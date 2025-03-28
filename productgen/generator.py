import random
import os
import csv
import io
import json
import requests
from pathlib import Path
from enum import Enum
from functools import lru_cache

# def fetch_data_from_dummyjson(self):
#     url = 'https://dummyjson.com/products'
#     response = requests.get(url)
#     response.raise_for_status()
#     return response.json().get("products", [])

    
class Style(Enum):
    """
    Enum class representing different styles for generating product names.

    Attributes:
    -----------
        SIMPLE_CONCAT : int
            A simple concatenation style, where category and subcategory are joined with a space.
        HYPHENATION : int
            A hyphenation style, joining category and subcategory with a hyphen.
        TITLE_CASE : int
            A title case style, converting category and subcategory to title case.
        CAPITALIZATION : int
            A capitalization style, capitalizing the first letter of category and subcategory.
        RANDOM_CAPITALIZATION : int
            A random capitalization style, randomly choosing uppercase or lowercase for category and subcategory.
        RANDOM_WORD_ORDER : int
            A random word order style, swapping the order of category and subcategory randomly.
    """
    SIMPLE_CONCAT = 1
    HYPHENATION = 2
    TITLE_CASE = 3
    CAPITALIZATION = 4
    RANDOM_CAPITALIZATION = 5
    RANDOM_WORD_ORDER = 6

class ProductGenConfig:
    """
    The ProductGenConfig class manages loading, saving, and updating a JSON configuration file. It is designed to store user-specific settings, such as custom product brands.
        - Table of Contents
        - Overview
        - Installation & Setup
        - Usage
        - Initialization
        - Loading Configuration
        - Saving Configuration
        - Adding Custom Brands

        Example
        - API Reference
    
    """

    def __init__(self, config_path=None):
        self.config_path = config_path or Path.home() / ".productgen" / "config.json"
        self.config = self.load_config()

    def load_config(self):
        """ Loads custom configuration settings from file"""
        if self.config_path.exists():
            with open(self.config_path, "r") as f:
                return json.load(f)
        return {}
    
    def save_config(self):
        """ Saves current configuration to file"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=2)

    def add_custom_brand(self, brand):
        """ Adds a custom brand to configuration"""
        if 'custom_brands' not in self.config:
            self.config['custom_brands'] = []
        if brand not in self.config['custom_brands']:
            self.config['custom_brands'].append(brand)
            self.save_config()

@lru_cache(maxsize=None)
def load_data_from_json(filename):
    """
    Loads a JSON file from the data folder and returns its contents.
    If the file does not exist, returns a default data structure (dict or list).
    """
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "data", filename)
    if not os.path.exists(data_path):
        # Return {} or [] depending on the expected data structure
        return {}
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

PRODUCT_BRANDS = load_data_from_json("product_brands.json").get("brands", [])
PRODUCT_CATEGORIES = load_data_from_json("product_categories.json").get("category", [])
MARKETING_TAGLINES = load_data_from_json("marketing_taglines.json").get("taglines", [])

def generate_random_word(language="en"):
    """
    Creates a random word from a-z (simple approach).
    """
    length = random.randint(3, 8)
    letters = "abcdefghijklmnopqrstuvwxyz"  # Could add logic for different languages
    return "".join(random.choice(letters) for i in range(length))

def set_random_seed(seed_value=None):
    """
    Sets the random seed for reproducible results. 
    If seed_value=None, it will use a random seed.
    """
    if seed_value is not None:
        random.seed(seed_value)

def build_markov_model(corpus, n=2):
    """
    Builds a Markov model (character-based) with n-gram.
    corpus: text data used as source
    n: length of the n-gram
    """
    model = {}
    for i in range(len(corpus) - n):
        gram = corpus[i:i+n]
        next_char = corpus[i+n]
        model.setdefault(gram, []).append(next_char)
    return model

def generate_word_markov(model, n=2, max_length=8):
    """
    Generates a random word from a character-based Markov model.
    n (int): the length of the n-gram
    max_length (int): the maximum length of the generated word
    """
    if not model:
        return "EmptyMarkov"

    # Start with a random gram
    start = random.choice(list(model.keys()))
    output = list(start)
    for _ in range(max_length - n):
        gram = "".join(output[-n:])
        if gram in model:
            output.append(random.choice(model[gram]))
        else:
            break
    return "".join(output).capitalize()

def generate_random_word_by_markov(corpus=None, length=80):
    """
    Example function to create a brand/product name via Markov Chain.
    Default corpus: concatenated PRODUCT_BRANDS.
    length: maximum number of characters.
    """
    if not corpus:
        corpus = "".join(PRODUCT_BRANDS)

    model = build_markov_model(corpus, n=2)
    return generate_word_markov(model, n=2, max_length=length)

def generate_marketing_taglines(style, taglines=None, use_suflix=False, use_tagline=False):
    """
    Generates a marketing tagline based on a specific style and additional options.
    """
    if taglines is None:
        taglines = random.choice(MARKETING_TAGLINES) if MARKETING_TAGLINES else "DefaultTagLine"

    # Currently this resets taglines to an empty string. Adjust logic as needed.
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
        words = taglines.split()
        random.shuffle(words)
        marketing_taglines = "".join(words)
    else:
        raise ValueError("Invalid Style")

    if use_suflix:
        marketing_taglines += f"{random.randint(100, 999)}"

    if use_tagline:
        extra_tagline = random.choice(MARKETING_TAGLINES) if MARKETING_TAGLINES else "Premium"
        marketing_taglines += f" | {extra_tagline}"
    
    return f"{marketing_taglines}"

def generate_product_category(style, category=None, use_suflix=False, use_tagLine=False):
    """
    Generates a product category string based on a specific style, using optional suffix or tagline.
    """
    if category is None:
        category = random.choice(PRODUCT_CATEGORIES) if PRODUCT_BRANDS else "DefaultCategory"
        
    # Currently these lines override category and subcategory with empty strings
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
    """
    Main function to generate a product name. Uses a style, optional brand, suffix, and tagline.
    """
    if brand is None:
        if PRODUCT_BRANDS:
            brand = random.choice(PRODUCT_BRANDS)
        else:
            brand = generate_random_word_by_markov()
    
    if PRODUCT_CATEGORIES:
        category = random.choice(list(PRODUCT_CATEGORIES.keys()))
        sub_list = PRODUCT_CATEGORIES[category]
        subcategory = random.choice(sub_list) if sub_list else "Generic"
    else:
        category = generate_random_word_by_markov()
        subcategory = generate_random_word_by_markov()

    # Currently these lines override the chosen category and subcategory
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
        tagline = random.choice(MARKETING_TAGLINES) if MARKETING_TAGLINES else "UltraX"
        product_name += f"{tagline} "

    return f"{brand} {product_name}"

def generate_product_description(category, subcategory, features_count = 3):
    """
        Generates a product description based on category and subcategory.

        Args : 
            category (str): The category of the product.
            subcategory (str): The subcategory of the product.
            features_count (int): The number of features to include in the description.

        Returns : 
            str : The generated product description.
    """

    features = {
        "Electronics" : {
            "High Performance", "Energy efficient", "Smart connectivity",
            "Premium build quality", "Advanced technology", "User friendly interface"
        },
        "Clothing" : {
            "Premium material", "Comfortable fit", "Stylish design",
            "Durable construction", "Easy care", "versatile style"
        }
    }
    
    category_features = features.get(category, ["Premium Quality", "Great Value", "Innovative Design"])
    selected_features = random.sample(category_features, min(features_count, len(category_features)))

    description = f"Introducing our {subcategory} from {category} collection."
    description += "This product offers " + ",".join(selected_features[:-1])
    description += f"and {selected_features[-1]}."

    return description

def export_products(products, format='json', output_path = None):
    """
        Exports generated products to various formats.

        Args : 
            product (list) : List of generated product names / details
            format (str) : Output format ('json', 'csv', 'txt')
            output_path (str) : Path to save the output file
    """

    if format == 'json':
        output = json.dumps(products, indent=2)
    elif format == 'csv':
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['name', 'category', 'subcategory', 'tagline'])
        for p in products:
            writer.writerow([p['name'], p['subcategory'], p.get('tagline', '')])
        output = output.getvalue()
    elif format == 'txt':
        output = "\n".join(str(p) for p in products)
    else:
        raise ValueError(f"Unsupported format : {format}")

    if output_path:
        with open(output_path, 'w') as f:
            f.write(output)
    return output
    

