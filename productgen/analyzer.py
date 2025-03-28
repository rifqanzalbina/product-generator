from textblob import TextBlob
import spacy

class ProductNameAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze_sentiment(self, product_name : str) -> dict:
        """ analyze sentiment and impact of product name"""
        blob = TextBlob(product_name)
        doc = self.nlp(product_name)

        return {
            "sentiment_score" : blob.sentiment.polarity,
            "subjectivity" : blob.sentiment.subjectivity,
            "memorability_score" : self._calculate_memorability(doc),
            "brand_compatibility" : self._check_brand_compatibility(doc)
        }
    
    def suggest_improvements(self, product_name : str) -> list:
        """ Suggest improvements for product name"""
        analysis = self.analyze_sentiment(product_name)
        suggestions = []

        if analysis["sentiment_score"] < 0.2:
            suggestions.append("Considerr using more positive words")
        if analysis["memorability_score"] < 0.5:
            suggestions.append("Add unique elements to make it more memorable")

        return suggestions

        
            
