from factory.ReceiptItemFactory import ReceiptItemFactory
from entity.Basket import Basket
from entity.Receipt import Receipt


class ReceiptFactory:

    @staticmethod
    def build(basket: Basket):
        basket_items = basket.get_items()
        receipt = ReceiptFactory.__build_receipt_by_basket_items(basket_items)
        return receipt

    @staticmethod
    def __build_receipt_by_basket_items(basket_items):
        receipt_items = []
        total_sales_taxes = 0
        total_amount = 0

        for basket_item in basket_items:
            receipt_item = ReceiptItemFactory.build(basket_item)
            receipt_items.append(receipt_item)
            total_amount += receipt_item.get_amount_in_cents()
            total_sales_taxes += receipt_item.get_sales_taxes_in_cents()

        receipt = Receipt(
            receipt_items=receipt_items,
            total_amount=total_amount,
            total_sales_taxes=total_sales_taxes
        )

        return receipt
