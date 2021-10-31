from entity.Category import Category
from entity.BasketItem import BasketItem
from entity.Tax import Tax
import math
from entity.ReceiptItem import ReceiptItem


class ReceiptItemMaker:

    @staticmethod
    def build(basket_item: BasketItem):
        product = basket_item.get_product()
        product_sales_taxes = ReceiptItemMaker.__calculate_product_sales_taxes(product=product)
        product_amount = ReceiptItemMaker.__calculate_product_amount(product=product, sales_taxes=product_sales_taxes)

        quantity = basket_item.get_quantity()
        basket_item_sales_taxes = product_sales_taxes * quantity
        basket_item_amount = product_amount * quantity

        receipt_item = ReceiptItem(
            product_title=product.get_title(),
            quantity=quantity,
            sales_taxes_in_cents=basket_item_sales_taxes,
            amount_in_cents=basket_item_amount
        )

        return receipt_item

    @staticmethod
    def __calculate_product_amount(*, product, sales_taxes):
        product_price = product.get_price()
        amount = product_price + sales_taxes
        return amount

    @staticmethod
    def __calculate_product_sales_taxes(product):
        sales_taxes_amount = 0
        if product.is_imported():
            sales_taxes_amount += ReceiptItemMaker.__get_tax_amount(product, tax=Tax.IMPORT)
        if not Category.is_basic_category(product.get_category()):
            sales_taxes_amount += ReceiptItemMaker.__get_tax_amount(product, tax=Tax.NON_BASIC_CATEGORY)
        return sales_taxes_amount

    @staticmethod
    def __get_tax_amount(product, tax: Tax):
        tax_amount = product.get_price() * tax.value / 100
        rounded_tax_amount = ReceiptItemMaker.__round(tax_amount)
        return rounded_tax_amount

    @staticmethod
    def __round(amount):
        nearest = 5  # 0.05 in full currency
        return math.ceil(amount / nearest) * nearest