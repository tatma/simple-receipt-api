from common import utils


def build(receipt_items, total_amount, total_sales_taxes):
    total_sales_taxes_in_units = utils.get_price_in_units(price_in_cents=total_sales_taxes)
    total_amount_in_units = utils.get_price_in_units(price_in_cents=total_amount)
    return {
        'items': receipt_items,
        'sales_taxes': total_sales_taxes_in_units,
        'total': total_amount_in_units
    }