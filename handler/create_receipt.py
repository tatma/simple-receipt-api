from common import utils
from factory.ReceiptResponseFactory import ReceiptResponseFactory
from exception.UnvalidValueException import UnvalidValueException
from exception.BadRequestException import BadRequestException
import json


def handler(event, context):

    try:
        items = get_items_by_event(event)
        body = ReceiptResponseFactory.build(items)
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

    return items_in_request
