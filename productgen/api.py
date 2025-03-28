from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from productgen import Style

app = FastAPI()

class ProductRequest(BaseModel):
    category: str
    style: str
    brand: str = None
    use_suffix: bool = False
    use_tagline: bool = False

@app.post("/generate")
async def generate_product(request: ProductRequest):
    try:
        style = Style[request.style.upper()]
        product = generate_product_name(
            style=style,
            brand=request.brand,
            use_suffix=request.use_suffix,
            use_tagline=request.use_tagline
        )
        return {"product_name": product}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/analyze/{product_name}")
async def analyze_product(product_name: str):
    analyzer = ProductNameAnalyzer()
    return analyzer.analyze_sentiment(product_name)