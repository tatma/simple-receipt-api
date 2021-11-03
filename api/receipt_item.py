from common import utils


def build(title, quantity, amount):
    amount_in_units = utils.get_price_in_units(price_in_cents=amount)
    return {
        'product' : title,
        'quantity' : quantity,
        'amount' : amount_in_units}