import api.receipt_item
import utils
from entity.Receipt import Receipt


def build(receipt: Receipt):
    api_receipt_items = build_receipt_items(receipt)
    total_sales_taxes_in_units = utils.get_price_in_units(price_in_cents=receipt.get_total_sales_taxes())
    total_amount_in_units = utils.get_price_in_units(price_in_cents=receipt.get_total_amount())
    return {
        'items': api_receipt_items,
        'sales_taxes': total_sales_taxes_in_units,
        'total': total_amount_in_units
    }


def build_receipt_items(receipt):
    api_receipt_items = []
    for receipt_item in receipt.get_receipt_items():
        api_receipt_item = api.receipt_item.build(receipt_item)
        api_receipt_items.append(api_receipt_item)
    return api_receipt_items