from entity.Basket import Basket
from entity.Product import Product
from entity.Category import Category
from handler.receipt.ReceiptMaker import ReceiptMaker
import api.receipt
from common import utils
import json


def handler(event, context):
    body = event['body']
    body_json = json.loads(body)
    items = body_json['items']

    basket = Basket()
    for item in items:
        product = Product(
            title=item['title'],
            price=item['price'] * 100,
            category=Category(item['category'].lower()),
            is_imported=False)
        basket.add(product=product, quantity=item['quantity'])

    receipt = ReceiptMaker.build(basket)
    body = api.receipt.build(receipt)
    return {
        'statusCode': 200,
        'body': utils.json_response(body),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
