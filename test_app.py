from handler import create_receipt
import json


payload = {
    "items": [
        {"title": "imported bottle of perfume", "category": "cosmetic", "quantity": 1, "price": 27.99, "imported": True},
        {"title": "bottle of perfume", "category": "cosmetic", "quantity": 1, "price": 18.99},
        {"title": "packet of headache pills", "category": "medical", "quantity": 1, "price": 9.75},
        {"title": "box of imported chocolates", "category": "food", "quantity": 3, "price": 11.25, "imported": True}
    ]
}
event = {'body': json.dumps(payload)}
resp = create_receipt.handler(event, None)
print(resp)