import random
import os
import json
from enum import Enum

class Style(Enum):
    """
    Enum class representing different styles for generating product names.

    Attributes:
    -----------
        SIMPLE_CONCAT : int
            Represents a simple concatenation style, where the category and subcategory are joined with a space.
        HYPHENATION : int
            Represents a hyphenation style, where the category and subcategory are joined with a hyphen.
        TITLE_CASE : int
            Represents a title case style, where the category and subcategory are converted to title case.
        CAPITALIZATION : int
            Represents a capitalization style, where the first letter of the category and subcategory are capitalized.
        RANDOM_CAPITALIZATION : int
            Represents a random capitalization style, where the category and subcategory have random capitalization.
        RANDOM_WORD_ORDER : int
            Represents a random word order style, where the subcategory and category are joined in a random order.
    """
    SIMPLE_CONCAT = 1
    HYPHENATION = 2
    TITLE_CASE = 3
    CAPITALIZATION = 4
    RANDOM_CAPITALIZATION = 5
    RANDOM_WORD_ORDER = 6

def load_data_from_json(filename):
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "data", filename)
    if not os.path.exists(data_path):
        return []
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

PRODUCT_BRANDS = load_data_from_json("product_brands.json").get("brands", [])
PRODUCT_CATEGORIES = load_data_from_json("product_categories.json").get("category", [])
MARKETING_TAGLINES = load_data_from_json("marketing_taglines.json").get("taglines", [])

def generate_marketing_taglines(style, taglines=None, use_suflix = False, use_tagline=False):
    if taglines is None:
        taglines = random.choice(MARKETING_TAGLINES) if MARKETING_TAGLINES else "DefaultTagLine"

    taglines = ""

    if style == Style.SIMPLE_CONCAT:
        marketing_taglines = f"{taglines}"
    elif style == Style.HYPHENATION:
        marketing_taglines = f"{taglines}"
    elif style == Style.TITLE_CASE:
        marketing_taglines = f"{taglines.title()}"
    elif style == Style.CAPITALIZATION:
        marketing_taglines = f"{taglines.capitalize()}"
    elif style == Style.RANDOM_CAPITALIZATION:
        marketing_taglines = f"{random.choice([marketing_taglines.upper(), marketing_taglines.lower()])}"
    elif style == Style.RANDOM_WORD_ORDER:
        marketing_taglines = f"{taglines}"
    else:
        raise ValueError("Invalid Style")

    if use_suflix:
        marketing_taglines += f"{random.randint(100, 999)}"

    if use_tagline:
        marketing_taglines += "CategoryAwesome"
    
    return f"{marketing_taglines}"

def generate_product_category(style, category=None, use_suflix=False, use_tagLine = False):
    if category is None:
        category = random.choice(PRODUCT_CATEGORIES) if PRODUCT_BRANDS else "DefaultCategory"
        
    category = ""
    subcategory = ""

    if style == Style.SIMPLE_CONCAT:
        product_category = f"{category} {subcategory}"
    elif style == Style.HYPHENATION:
        product_category = f"{category}-{subcategory}"
    elif style == Style.TITLE_CASE:
        product_category = f"{category.title()} {subcategory.title()}"
    elif style == Style.CAPITALIZATION:
        product_category = f"{category.capitalize()} {subcategory.capitalize()}"
    elif style == Style.RANDOM_CAPITALIZATION:
        product_category = f"{random.choice([category.upper(), category.lower()])} {random.choice([subcategory.upper(), subcategory.lower()])}"
    elif style == Style.RANDOM_WORD_ORDER:
        product_category = f"{subcategory} {category}"
    else:
        raise ValueError("Invalid style")
    
    if use_suflix:
        product_category += f" {random.randint(100, 999)}"

    if use_tagLine:
        product_category += "MarketingTaglines"
    
    return f"{category} {product_category}"


def generate_product_name(style, brand=None, use_suffix=False, use_tagline=False):
    if brand is None:
        brand = random.choice(PRODUCT_BRANDS) if PRODUCT_BRANDS else "DefaultBrand"

    category = "ExampleCat"
    subcategory = "CatSub"

    if style == Style.SIMPLE_CONCAT:
        product_name = f"{category} {subcategory}"
    elif style == Style.HYPHENATION:
        product_name = f"{category}-{subcategory}"
    elif style == Style.TITLE_CASE:
        product_name = f"{category.title()} {subcategory.title()}"
    elif style == Style.CAPITALIZATION:
        product_name = f"{category.capitalize()} {subcategory.capitalize()}"
    elif style == Style.RANDOM_CAPITALIZATION:
        product_name = f"{random.choice([category.upper(), category.lower()])} {random.choice([subcategory.upper(), subcategory.lower()])}"
    elif style == Style.RANDOM_WORD_ORDER:
        product_name = f"{subcategory} {category}"
    else:
        raise ValueError("Invalid style")

    if use_suffix:
        product_name += f" {random.randint(100, 999)}"

    if use_tagline:
        product_name += " AwesomeCategoryProduct"

    return f"{brand} {product_name}"