class BasketItem:

    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity