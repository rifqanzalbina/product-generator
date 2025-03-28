from datetime import datetime
import sqlite3

class ProductManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self._init_db()

    def save_product(self, 
                    name: str, 
                    category: str, 
                    metadata: dict = None) -> int:
        """Save generated product details"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO products (name, category, metadata, created_at)
            VALUES (?, ?, ?, ?)
        """, (name, category, str(metadata), datetime.now()))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_product_history(self, category : str = None, limit : int = 100) -> list:
        """ Retrievve product generation history"""
        cursor = self.conn.cursor()
        query = "SELECT * FROM products"
        if category : 
            query += " WHERE category = ?"
            cursor.execute(query, (category,))
        else:
            cursor.execute(query)
        return cursor.fetchmany(limit)
    

