from entity.Category import Category
from factory.ProductFactory import ProductFactory


class TestEntityValidation:


    def test_building_of_basic_non_imported_product(self):
        data = {
            'title': 'IT by Stephen King',
            'category': 'book',
            'price': '10.22',
            'quantity': 3,
            'imported': False
        }
        product = ProductFactory.build(
            title=data['title'],
            category=data['category'],
            price_in_units=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
            product.get_category() is Category.BOOK and \
            product.get_price() == data['price'] * 100 and \
            product.is_imported() is False and \
            Category.is_basic_category(product.get_category()) is True
        
    def test_building_of_basic_imported_product(self):
        data = {
            'title': 'Imported IT by Stephen King',
            'category': 'book',
            'price': '10.22',
            'quantity': 3,
            'imported': True
        }
        product = ProductFactory.build(
            title=data['title'],
            category=data['category'],
            price_in_units=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
               product.get_category() is Category.BOOK and \
               product.get_price() == data['price'] * 100 and \
               product.is_imported() is True and \
               Category.is_basic_category(product.get_category()) is True

    def test_building_of_non_basic_non_imported_product(self):
        data = {
            'title': 'Soap',
            'category': 'cosmetic',
            'price': '5.40',
            'quantity': 1,
            'imported': False
        }
        product = ProductFactory.build(
            title=data['title'],
            category=data['category'],
            price_in_units=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
               product.get_category() is Category.COSMETIC and \
               product.get_price() == data['price'] * 100 and \
               product.is_imported() is False and \
               Category.is_basic_category(product.get_category()) is False

    def test_building_of_non_basic_imported_product(self):
        data = {
            'title': 'Imported Soap',
            'category': 'cosmetic',
            'price': '5.40',
            'quantity': 1,
            'imported': True
        }
        product = ProductFactory.build(
            title=data['title'],
            category=data['category'],
            price_in_units=data['price'],
            is_imported=data['imported'])

        assert product.get_title() == data['title'] and \
               product.get_category() is Category.COSMETIC and \
               product.get_price() == data['price'] * 100 and \
               product.is_imported() is True and \
               Category.is_basic_category(product.get_category()) is False

    def test_imported_flag_omission(self):
        data = {
            'title': 'White Chocolate',
            'category': 'food',
            'price': '0.95',
            'quantity': 1
        }

        product = ProductFactory.build(
            title=data['title'],
            category=data['category'],
            price_in_units=data['price'])

        assert product.get_title() == data['title'] and \
            product.get_category() is Category.FOOD and \
            product.get_price() == data['price'] * 100 and \
            product.is_imported() is False
