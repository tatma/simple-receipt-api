from validator.ReceiptRequestValidator import ReceiptRequestValidator
from common import utils
from entity.Category import Category
from entity.Tax import Tax
import api.receipt_item
import api.receipt


class ReceiptResponseFactory:

    @staticmethod
    def build(items):

        receipt_items = []
        total_amount = 0
        total_sales_taxes = 0

        for item in items:

            ReceiptRequestValidator.parse_item(item)

            item = ReceiptResponseFactory.__get_normalized_item(item)

            sales_taxes = ReceiptResponseFactory.__calculate_sales_taxes(item=item)

            total_item_amount = ReceiptResponseFactory.__get_total_item_amount(
                price_in_cents=item['price_in_cents'],
                sales_taxes=sales_taxes,
                quantity=item['quantity'])

            total_item_sales_taxes = ReceiptResponseFactory.__get_total_sales_taxes(
                sales_taxes=sales_taxes,
                quantity=item['quantity'])

            receipt_item = api.receipt_item.build(
                title=item['title'],
                quantity=item['quantity'],
                amount=total_item_amount)

            total_amount += total_item_amount
            total_sales_taxes += total_item_sales_taxes

            receipt_items.append(receipt_item)

        return api.receipt.build(receipt_items, total_amount=total_amount, total_sales_taxes=total_sales_taxes)

    @staticmethod
    def __get_normalized_item(item):
        if 'imported' not in item: item['imported'] = False
        item['price_in_cents'] = utils.get_price_in_cents(price_in_units=item['price'])
        del item['price']
        return item

    @staticmethod
    def __calculate_sales_taxes(item):
        sales_taxes_amount = 0
        if item['imported']:
            sales_taxes_amount += utils.get_rounded_tax_amount(item['price_in_cents'], tax=Tax.IMPORT)
        if not Category.is_basic_category(item['category']):
            sales_taxes_amount += utils.get_rounded_tax_amount(item['price_in_cents'], tax=Tax.NON_BASIC_CATEGORY)
        return sales_taxes_amount

    @staticmethod
    def __get_total_item_amount(price_in_cents, sales_taxes, quantity):
        item_amount = price_in_cents + sales_taxes
        total_item_amount = item_amount * quantity
        return total_item_amount

    @staticmethod
    def __get_total_sales_taxes(sales_taxes, quantity):
        total_sales_taxes = quantity * sales_taxes
        return total_sales_taxes

