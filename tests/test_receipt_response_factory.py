from validator.ReceiptRequestValidator import ReceiptRequestValidator
from exception.UnvalidValueException import UnvalidValueException
import pytest
from factory.ReceiptResponseFactory import ReceiptResponseFactory


class TestReceiptRequestValidator:

    def test_input_1(self):
        items = [
                {"title": "imported bottle of perfume", "category": "cosmetic", "quantity": 1, "price": 27.99,
                 "imported": True},
                {"title": "bottle of perfume", "category": "cosmetic", "quantity": 1, "price": 18.99},
                {"title": "packet of headache pills", "category": "medical", "quantity": 1, "price": 9.75},
                {"title": "box of imported chocolates", "category": "food", "quantity": 3, "price": 11.25,
                 "imported": True}
            ]
        body = ReceiptResponseFactory.build(items)

        assert body == {
            "items": [
                {
                    "product": "imported bottle of perfume",
                    "quantity": 1,
                    "amount": 32.19
                },
                {
                    "product": "bottle of perfume",
                    "quantity": 1,
                    "amount": 20.89
                },
                {
                    "product": "packet of headache pills",
                    "quantity": 1,
                    "amount": 9.75
                },
                {
                    "product": "box of imported chocolates",
                    "quantity": 3,
                    "amount": 35.55
                }
            ],
            "sales_taxes": 7.9,
            "total": 98.38
        }

    def test_input_2(self):
        items = [
            {"title": "imported box of chocolates", "category": "food", "quantity": 1, "price": 10.00, "imported": True},
            {"title": "imported bottle of perfume", "category": "cosmetic", "quantity": 1, "price": 47.50, "imported": True}
        ]
        body = ReceiptResponseFactory.build(items)

        assert body == {
            "items": [
                {
                    "product": "imported box of chocolates",
                    "quantity": 1,
                    "amount": 10.5
                },
                {
                    "product": "imported bottle of perfume",
                    "quantity": 1,
                    "amount": 54.65
                }
            ],
            "sales_taxes": 7.65,
            "total": 65.15
        }

    def test_input_3(self):
        items = [
            {"title": "imported bottle of perfume", "category": "cosmetic", "quantity": 1, "price": 27.99, "imported": True},
            {"title": "bottle of perfume", "category": "cosmetic", "quantity": 1, "price": 18.99},
            {"title": "packet of headache pills", "category": "medical", "quantity": 1, "price": 9.75},
            {"title": "box of imported chocolates", "category": "food", "quantity": 3, "price": 11.25, "imported": True}
        ]
        body = ReceiptResponseFactory.build(items)

        assert body == {
            "items": [
                {
                    "product": "imported bottle of perfume",
                    "quantity": 1,
                    "amount": 32.19
                },
                {
                    "product": "bottle of perfume",
                    "quantity": 1,
                    "amount": 20.89
                },
                {
                    "product": "packet of headache pills",
                    "quantity": 1,
                    "amount": 9.75
                },
                {
                    "product": "box of imported chocolates",
                    "quantity": 3,
                    "amount": 35.55
                }
            ],
            "sales_taxes": 7.9,
            "total": 98.38
        }