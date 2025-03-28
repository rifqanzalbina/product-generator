class SEOOptimizer:
    def __init__(self):
        self.keyword_data = self._load_keyword_data()
    
    def optimize_product_name(self, 
                            product_name: str, 
                            category: str) -> dict:
        """Optimize product name for SEO"""
        analysis = {
            "length": self._check_length(product_name),
            "keyword_density": self._analyze_keywords(product_name, category),
            "readability": self._check_readability(product_name),
            "url_friendly": self._is_url_friendly(product_name)
        }
        
        suggestions = self._generate_seo_suggestions(analysis)
        return {
            "analysis": analysis,
            "suggestions": suggestions,
            "seo_score": self._calculate_seo_score(analysis)
        }

    def suggest_keywords(self, category : str, subcategory : str) -> list:
        """ Suggest relevant keywords for the product name"""
        return self._get_trending_keywords(category, subcategory)