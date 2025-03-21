"""
texstat_id - Library untuk analisis statistik teks Bahasa Indonesia
"""

# Import fungsi-fungsi langsung ke namespace package
from .generator import generate_product_name, Style


__version__ = '0.0.1'
__all__ = [
    'generate_product_name',
    'Style'
]