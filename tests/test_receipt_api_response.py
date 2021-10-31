from entity.Basket import Basket
from entity.Product import Product
from entity.Category import Category
from factory.ReceiptFactory import ReceiptFactory
import api.receipt


class TestReceiptApiResponse:

    def test_non_imported_products(self):
        basket = Basket()

        product = Product(
            title='The Book',
            price=1249,
            category=Category.BOOK,
            is_imported=False)
        basket.add(product=product, quantity=2)

        product = Product(
            title='Music CD',
            price=1499,
            category=Category.ENTERTAINMENT,
            is_imported=False)
        basket.add(product=product, quantity=1)

        product = Product(
            title='Chocolate',
            price=85,
            category=Category.FOOD,
            is_imported=False)
        basket.add(product=product, quantity=1)

        receipt = ReceiptFactory.build(basket)
        api_receipt = api.receipt.build(receipt)

        assert api_receipt == {'items': [{'product': 'The Book', 'quantity': 2, 'amount': 24.98},
                                         {'product': 'Music CD', 'quantity': 1, 'amount': 16.49},
                                         {'product': 'Chocolate', 'quantity': 1, 'amount': 0.85}],
                               'sales_taxes': 1.5,
                               'total': 42.32}

    def test_single_imported_products(self):
        basket = Basket()

        product = Product(
            title='Imported Box of Chocolate',
            price=1000,
            category=Category.FOOD,
            is_imported=True)
        basket.add(product=product, quantity=1)

        product = Product(
            title='Imported bottle of Perfume',
            price=4750,
            category=Category.COSMETIC,
            is_imported=True)
        basket.add(product=product, quantity=1)

        receipt = ReceiptFactory.build(basket)
        api_receipt = api.receipt.build(receipt)

        assert api_receipt == {'items': [{'product': 'Imported Box of Chocolate', 'quantity': 1, 'amount': 10.5},
                                         {'product': 'Imported bottle of Perfume', 'quantity': 1, 'amount': 54.65}],
                               'sales_taxes': 7.65,
                               'total': 65.15}

    def test_multiple_imported_products(self):
        basket = Basket()

        product = Product(
            title='Imported bottle of Perfume',
            price=2799,
            category=Category.COSMETIC,
            is_imported=True)
        basket.add(product=product, quantity=1)

        product = Product(
            title='Bottle of Perfume',
            price=1899,
            category=Category.COSMETIC,
            is_imported=False)
        basket.add(product=product, quantity=1)

        product = Product(
            title='Headache Pills',
            price=975,
            category=Category.MEDICAL,
            is_imported=False)
        basket.add(product=product, quantity=1)

        product = Product(
            title='Imported Chocolate',
            price=1125,
            category=Category.FOOD,
            is_imported=True)
        basket.add(product=product, quantity=3)

        receipt = ReceiptFactory.build(basket)
        api_receipt = api.receipt.build(receipt)

        assert api_receipt == {'items': [{'product': 'Imported bottle of Perfume', 'quantity': 1, 'amount': 32.19},
                                         {'product': 'Bottle of Perfume', 'quantity': 1, 'amount': 20.89},
                                         {'product': 'Headache Pills', 'quantity': 1, 'amount': 9.75},
                                         {'product': 'Imported Chocolate', 'quantity': 3, 'amount': 35.55}],
                               'sales_taxes': 7.9,
                               'total': 98.38}
