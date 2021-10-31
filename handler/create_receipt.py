import api.receipt
from common import utils
from entity.Basket import Basket
from entity.Product import Product
from entity.Category import Category
from factory.ReceiptFactory import ReceiptFactory
from validator.ReceiptRequestValidator import ReceiptRequestValidator
from exception.UnvalidValueException import UnvalidValueException
from exception.BadRequestException import BadRequestException
import json


def handler(event, context):

    try:
        items = get_items_by_event(event)
        basket = build_basked_by_request(items)
        receipt = ReceiptFactory.build(basket)
        body = api.receipt.build(receipt)
        status_code = 201

    except UnvalidValueException as e:
        body = {'message': str(e)}
        status_code = 400

    except BadRequestException as e:
        body = {'message': 'Your request is not valid.'}
        status_code = 400

    except Exception as e:
        raise e

    return {
        'statusCode': status_code,
        'body': utils.json_response(body),
        'headers': {
            'Content-Type': 'application/json'
        }
    }


def get_items_by_event(event):
    try:
        body = event['body']
        body_json = json.loads(body)
        items_in_request = body_json['items']
    except:
        raise BadRequestException('Your request is invalid')

    items = parse_items_in_request(items_in_request)

    return items


def parse_items_in_request(items_in_request):
    items = []
    for item in items_in_request:
        if 'imported' not in item: item['imported'] = False
        ReceiptRequestValidator.parse_item(item)
        items.append(item)
    return items


def build_basked_by_request(items):
    basket = Basket()
    for item in items:
        category = Category(item['category'].lower())
        price_in_cents = utils.get_price_in_cents(price_in_units=item['price'])
        product = Product(
            title=item['title'],
            price_in_cents=price_in_cents,
            category=category,
            is_imported=item['imported'])
        basket.add(product=product, quantity=item['quantity'])
    return basket
