from transformers import pipeline
from typing import List, Dict, Optional
from .generator import Style

class AIProductGenerator:
    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2')

    def generative_creative_names(self, 
                                  category: str, 
                                  brand: Optional[str] = None,
                                  style: Style = Style.TITLE_CASE,
                                  num_suggestions: int = 5) -> List[str]:
        prompt = f"Generate {num_suggestions} creative product names for a {category}"
        if brand:
            prompt += f" from the brand {brand}"
        
        results = self.generator(prompt, max_length=50, num_return_sequences=num_suggestions)
        names = [result['generated_text'].split('\n')[0] for result in results]
        
        if style == Style.TITLE_CASE:
            names = [name.title() for name in names]
        elif style == Style.ALL_CAPS:
            names = [name.upper() for name in names]
        
        return names

    def generate_product_story(self, 
                               product_name: str,
                               max_length: int = 200) -> str:
        prompt = f"Write a short product story for {product_name}:"
        result = self.generator(prompt, max_length=max_length, num_return_sequences=1)
        return result[0]['generated_text']

    def generate_product_features(self,
                                  product_name: str,
                                  category: str,
                                  num_features: int = 5) -> List[str]:
        prompt = f"List {num_features} features of {product_name}, a {category}:"
        result = self.generator(prompt, max_length=200, num_return_sequences=1)
        features = result[0]['generated_text'].split('\n')[1:]  # Skip the prompt
        return features[:num_features]

    def analyze_name_effectiveness(self, product_name: str) -> Dict[str, float]:
        # This is a simplified version. In a real scenario, you might want to use
        # a sentiment analysis model or more sophisticated metrics.
        return {
            "memorability": len(product_name) / 10,  # Simplified metric
            "uniqueness": len(set(product_name.lower())) / len(product_name),
            "brand_fit": 0.7,  # Placeholder value
            "market_appeal": 0.8,  # Placeholder value
        }

    def batch_generate_names(self,
                             categories: List[str],
                             brand: Optional[str] = None,
                             max_workers: int = 3) -> Dict[str, List[str]]:
        results = {}
        for category in categories:
            results[category] = self.generative_creative_names(category, brand)
        return results