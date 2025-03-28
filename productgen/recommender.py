from .generator import Style
from collections import Counter
import numpy as np

class ProductNameRecommender:
    def __init__(self):
        self.ratings = {}
        self.popular_combinations = Counter()

    def rate_product_name(self, product_name : str, rating : int):
        """ Rate a product name (1-5 stars)"""

        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self.ratings[product_name] = rating

    def analyze_successful_patterns(self):
        """ Analyze highly rated names to find succesful patterns"""
        successfull_names = [name for name, rating in self.ratings.items() if rating >= 4]
        return self._extract_patterns(successfull_names)
    
    def get_recommendations(self, category : str, style : Style) -> list:
        """ Get recommended produt names based on historical ratings"""
        patterns = self.analyze_successful_patterns()
        return self._generate_with_patterns(category, style, patterns)

    