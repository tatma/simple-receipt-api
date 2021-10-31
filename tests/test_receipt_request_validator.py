from validator.ReceiptRequestValidator import ReceiptRequestValidator
from exception.UnvalidValueException import UnvalidValueException
import pytest


class TestReceiptRequestValidator:

    def test_validation_of_imported_product(self):
        item = {
            'title': 'Hung up by Salt',
            'price': 9.80,
            'category': 'entertainment',
            'imported': True
        }
        ReceiptRequestValidator.parse_item(item)
        assert True

    def test_validation_of_non_imported_product(self):
        item = {
            'title': 'Hung up by Salt',
            'price': 9.80,
            'category': 'entertainment',
            'imported': False
        }
        ReceiptRequestValidator.parse_item(item)
        assert True

    def test_unvalid_value_of_title(self):
        with pytest.raises(UnvalidValueException):
            item = {
                'title': 234,
                'price': 9.80,
                'category': 'entertainment',
                'imported': False
            }
            ReceiptRequestValidator.parse_item(item)

    def test_empty_value_of_title(self):
        with pytest.raises(UnvalidValueException):
            item = {
                'title': None,
                'price': 9.80,
                'category': 'entertainment',
                'imported': False
            }
            ReceiptRequestValidator.parse_item(item)

    def test_non_numeric_price(self):
        with pytest.raises(UnvalidValueException):
            item = {
                'title': 'Hung up by Salt',
                'price': '8.45',
                'category': 'entertainment',
                'imported': False
            }
            ReceiptRequestValidator.parse_item(item)

    def test_unvalid_format_of_price(self):
        with pytest.raises(UnvalidValueException):
            item = {
                'title': 'Hung up by Salt',
                'price': 10,
                'category': 'entertainment',
                'imported': False
            }
            ReceiptRequestValidator.parse_item(item)

    def test_unexisting_category(self):
        with pytest.raises(UnvalidValueException):
            item = {
                'title': 'Hung up by Salt',
                'price': 9.80,
                'category': 'whatisthis',
                'imported': False
            }
            ReceiptRequestValidator.parse_item(item)

    def test_unvalid_is_imported(self):
        with pytest.raises(UnvalidValueException):
            item = {
                'title': 'Hung up by Salt',
                'price': 9.80,
                'category': 'entertainment',
                'imported': 'true'
            }
            ReceiptRequestValidator.parse_item(item)