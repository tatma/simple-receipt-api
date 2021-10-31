from exception.UnvalidValueException import UnvalidValueException
from entity.Category import Category


class ReceiptRequestValidator:

    @staticmethod
    def parse_item(item):
        ReceiptRequestValidator.__validate_title(item['title'])
        ReceiptRequestValidator.__validate_price(item['price'])
        ReceiptRequestValidator.__validate_category(item['category'])
        ReceiptRequestValidator.__validate_is_imported(item['imported'])
        ReceiptRequestValidator.__validate_quantity(item['quantity'])
        return item

    @staticmethod
    def __validate_title(title):
        if not isinstance(title, str) or title.strip() == '':
            raise UnvalidValueException('Title must be a non-empty string')

    @staticmethod
    def __validate_price(price):
        if not isinstance(price, float):
            raise UnvalidValueException('Price must be a float number')

    @staticmethod
    def __validate_category(category):
        try:
            Category(category.lower())
        except:
            raise UnvalidValueException(f'Category is not valid. Accepted values: {[cat.value for cat in list(Category)]}')

    @staticmethod
    def __validate_is_imported(is_imported):
        if not isinstance(is_imported, bool):
            raise UnvalidValueException('Imported is not valid. Accepted values: [true, false]')

    @staticmethod
    def __validate_quantity(quantity):
        if not isinstance(quantity, int):
            raise UnvalidValueException('Quantity must be an integer number')
