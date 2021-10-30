from enum import Enum


class Category(Enum):
    FOOD = 'Food'
    BOOKS = 'Book'
    MEDICAL = 'Medical'
    COSMETICS = 'Cosmetics'
    ENTERTAINMENT = 'Entertainment'
    OTHER = 'Other'

    @staticmethod
    def is_basic_category(category):
        return category in [Category.FOOD, Category.BOOKS, Category.MEDICAL]