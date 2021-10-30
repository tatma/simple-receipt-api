class ReceiptItem:

    def __init__(self, product_title, quantity, sales_taxes_in_cents, amount_in_cents):
        self.__product_title = product_title
        self.__quantity = quantity
        self.__sales_taxes_in_cents = sales_taxes_in_cents
        self.__amount_in_cents = amount_in_cents

    def get_product_title(self):
        return self.__product_title

    def get_quantity(self):
        return self.__quantity

    def get_price_in_cents(self):
        return self.__price_in_cents

    def get_sales_taxes_in_cents(self):
        return self.__sales_taxes_in_cents

    def get_amount_in_cents(self):
        return self.__amount_in_cents
