from enum import Enum


class Category(Enum):
    FOOD = 'food'
    BOOK = 'book'
    MEDICAL = 'medical'
    COSMETIC = 'cosmetic'
    ENTERTAINMENT = 'entertainment'
    OTHER = 'other'

    @staticmethod
    def is_basic_category(category):
        return category in [Category.FOOD, Category.BOOK, Category.MEDICAL]
