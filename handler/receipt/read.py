from handler.receipt.ReceiptMaker import ReceiptMaker
import api.receipt

def lambda_handler(event, context):

    basket_id = 'from-event'
    basket = read_basket_from_db(basket_id)

    # receipt_item = api.receipt_items.build(
    #     product_title=product.get_title(),
    #     quantity=quantity,
    #     price_in_cents=basket_item_amount
    # )

    receipt = ReceiptMaker.build(basket)
    receipt_response = api.receipt.build(receipt)

    status_code = None
    body = None
    return {
        'statusCode': status_code,
        'body': receipt_response
    }