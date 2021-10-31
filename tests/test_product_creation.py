from entity.Category import Category
from entity.Product import Product


class TestEntityValidation:


    def test_building_of_basic_non_imported_product(self):
        data = {
            'title': 'IT by Stephen King',
            'category': Category('book'),
            'price': 1022,
            'quantity': 3,
            'imported': False
        }
        product = Product(
            title=data['title'],
            category=data['category'],
            price_in_cents=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
            product.get_category() is Category.BOOK and \
            product.get_price_in_cents() == data['price'] and \
            product.is_imported() is False and \
            Category.is_basic_category(product.get_category()) is True

    def test_building_of_basic_imported_product(self):
        data = {
            'title': 'Imported IT by Stephen King',
            'category': Category('book'),
            'price': 1022,
            'quantity': 3,
            'imported': True
        }
        product = Product(
            title=data['title'],
            category=data['category'],
            price_in_cents=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
               product.get_category() is Category.BOOK and \
               product.get_price_in_cents() == data['price'] and \
               product.is_imported() is True and \
               Category.is_basic_category(product.get_category()) is True

    def test_building_of_non_basic_non_imported_product(self):
        data = {
            'title': 'Soap',
            'category': Category('cosmetic'),
            'price': 540,
            'quantity': 1,
            'imported': False
        }
        product = Product(
            title=data['title'],
            category=data['category'],
            price_in_cents=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
               product.get_category() is Category.COSMETIC and \
               product.get_price_in_cents() == data['price'] and \
               product.is_imported() is False and \
               Category.is_basic_category(product.get_category()) is False

    def test_building_of_non_basic_imported_product(self):
        data = {
            'title': 'Imported Soap',
            'category': Category('cosmetic'),
            'price': 540,
            'quantity': 1,
            'imported': True
        }
        product = Product(
            title=data['title'],
            category=data['category'],
            price_in_cents=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
               product.get_category() is Category.COSMETIC and \
               product.get_price_in_cents() == data['price'] and \
               product.is_imported() is True and \
               Category.is_basic_category(product.get_category()) is False

    def test_imported_flag_omission(self):
        data = {
            'title': 'White Chocolate',
            'category': Category('food'),
            'price': 95,
            'quantity': 1
        }

        product = Product(
            title=data['title'],
            category=data['category'],
            price_in_cents=data['price'])

        assert product.get_title() == data['title'] and \
            product.get_category() is Category.FOOD and \
            product.get_price_in_cents() == data['price'] and \
            product.is_imported() is False
