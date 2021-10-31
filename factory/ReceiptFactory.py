from handler.receipt.ReceiptItemMaker import ReceiptItemMaker
from entity.Basket import Basket
from entity.Receipt import Receipt


class ReceiptMaker:

    @staticmethod
    def build(basket: Basket):
        items = basket.get_items()
        receipt = ReceiptMaker.__get_receipt(items)
        return receipt

    @staticmethod
    def __get_receipt(basket_items):
        receipt_items = []
        total_sales_taxes = 0
        total_amount = 0
        for basket_item in basket_items:
            receipt_item = ReceiptItemMaker.build(basket_item)
            receipt_items.append(receipt_item)
            total_amount += receipt_item.get_amount_in_cents()
            total_sales_taxes += receipt_item.get_sales_taxes_in_cents()

        receipt = Receipt(
            receipt_items=receipt_items,
            total_amount=total_amount,
            total_sales_taxes=total_sales_taxes
        )

        return receipt
