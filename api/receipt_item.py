from common import utils
from entity.ReceiptItem import ReceiptItem


def build(receipt_item: ReceiptItem):
    amount_in_units = utils.get_price_in_units(price_in_cents=receipt_item.get_amount_in_cents())
    return {
        'product': receipt_item.get_product_title(),
        'quantity': receipt_item.get_quantity(),
        'amount': amount_in_units
    }