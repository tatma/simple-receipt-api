def get_price_in_units(*, price_in_cents):
    return price_in_cents / 100

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