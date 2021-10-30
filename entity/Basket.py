from entity.BasketItem import BasketItem
import uuid


class Basket:

    def __init__(self):
        self.__items = []
        self.__id = uuid.uuid4().hex.upper()

    def add(self, *, product, quantity: int):
        basket_item = BasketItem(product=product, quantity=quantity)
        self.__items.append(basket_item)

    def get_items(self):
        return self.__items

    def get_id(self):
        return self.__id