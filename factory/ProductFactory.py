from common import utils
from entity.Category import Category
from entity.Product import Product


class ProductFactory:

    @staticmethod
    def build(title, category, price_in_units, is_imported=False):
        category = Category(category.lower())
        price_in_cents = utils.get_price_in_cents(price_in_units=price_in_units)
        product = Product(
            title=title,
            price=price_in_cents,
            category=category,
            is_imported=is_imported)
        return product
