from entity.BasketItem import BasketItem


class Basket:

    def __init__(self):
        self.__items = []

    def add(self, *, product, quantity: int):
        basket_item = BasketItem(product=product, quantity=quantity)
        self.__items.append(basket_item)

    def get_items(self):
        return self.__items