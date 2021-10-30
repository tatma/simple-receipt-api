class Receipt:

    def __init__(self, receipt_items, total_amount, total_sales_taxes):
        self.__receipt_items = receipt_items
        self.__total_amount = total_amount
        self.__total_sales_taxes = total_sales_taxes

    def get_receipt_items(self):
        return self.__receipt_items

    def get_total_amount(self):
        return self.__total_amount

    def get_total_sales_taxes(self):
        return self.__total_sales_taxes
