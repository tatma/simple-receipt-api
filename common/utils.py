def get_price_in_units(*, price_in_cents):
    return price_in_cents / 100


def get_price_in_cents(*, price_in_units):
    return price_in_units * 100


def json_response(obj):
    import json
    return json.dumps(obj, default=decimal_type)


def decimal_type(obj):
    from decimal import Decimal
    if isinstance(obj, Decimal):
        if float(obj).is_integer():
            return int(obj)
        else:
            return float(obj)
    raise TypeError


def calculate_tax_amount(price_in_cents, tax_value):
    tax_amount = price_in_cents * tax_value / 100
    return tax_amount


def round(price_in_cents):
    import math
    nearest = 5  # 0.05 in units
    return math.ceil(price_in_cents / nearest) * nearest

def get_rounded_tax_amount(price_in_cents, tax):
    tax_amount =calculate_tax_amount(price_in_cents=price_in_cents, tax_value=tax.value)
    rounded_tax_amount = round(price_in_cents=tax_amount)
    return rounded_tax_amount
