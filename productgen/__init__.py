"""
texstat_id - Library untuk analisis statistik teks Bahasa Indonesia
"""

# Import fungsi-fungsi langsung ke namespace package
from .generator import generate_product_name, Style
from .ai_generator import AIProductGenerator
from .recommender import ProductNameRecommender


__version__ = '0.0.1'
__all__ = [
    'generate_product_name',
    'Style',
    'AIProductGenerator',
    'ProductNameRecommender'
]