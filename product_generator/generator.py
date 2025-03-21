import random
from enum import Enum

class Style(Enum):
    SIMPLE_CONCAT = 1
    HYPHENATION = 2
    TITLE_CASE = 3
    CAPITALIZATION = 4
    RANDOM_CAPITALIZATION = 5
    RANDOM_WORD_ORDER = 6

# Define a list of product categories and subcategories
PRODUCT_CATEGORIES = {
    'Electronics': ['Smartphones', 'Laptops', 'Tablets', 'Headphones'],
    'Clothing': ['T-Shirts', 'Pants', 'Shirts', 'Jackets'],
    'Home & Garden': ['Furniture', 'Kitchenware', 'Decor', 'Outdoor'],
    'Books': ['Fiction', 'Non-Fiction', 'Children', 'Mystery'],
    'Sports': ['Football', 'Basketball', 'Tennis', 'Golf'],
}

def generate_product_name(style):
    category = random.choice(list(PRODUCT_CATEGORIES.keys()))
    subcategory = random.choice(PRODUCT_CATEGORIES[category])

    if style == Style.SIMPLE_CONCAT:
        return f"{category} {subcategory}"
    elif style == Style.HYPHENATION:
        return f"{category}-{subcategory}"
    elif style == Style.TITLE_CASE:
        return f"{category.title()} {subcategory.title()}"
    elif style == Style.CAPITALIZATION:
        return f"{category.capitalize()} {subcategory.capitalize()}"
    elif style == Style.RANDOM_CAPITALIZATION:
        return f"{random.choice([category.lower(), category.upper()])} {random.choice([subcategory.lower(), subcategory.upper()])}"
    elif style == Style.RANDOM_WORD_ORDER:
        return f"{subcategory} {category}"
    else:
        raise ValueError("Invalid style")