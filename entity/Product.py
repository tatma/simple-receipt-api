class Product:

    def __init__(self, code, title, price, category, is_imported=False):
        self.__code = code
        self.__title = title
        self.__price = price
        self.__category = category
        self.__is_imported = is_imported

    def get_slug(self) -> str:
        return self.__code

    def get_title(self) -> str:
        return self.__title

    def get_price(self) -> float:
        return self.__price

    def get_category(self):
        return self.__category

    def is_imported(self) -> bool:
        return self.__is_imported
