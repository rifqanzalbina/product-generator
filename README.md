# product generator

## Install 

```python
pip install productgen
```


## What can do?
- Make a product name automatically



# How To Usage ?

```py
# file: example_usage.py
from productgen.generator import generate_product_name, Style

def main():
    product_1 = generate_product_name(Style.SIMPLE_CONCAT)
    print("Contoh nama produk:", product_1)

    product_2 = generate_product_name(Style.TITLE_CASE, brand="MyBrand", use_suffix=True, use_tagline=True)
    print("Contoh nama produk dengan brand, suffix, dan tagline:", product_2)

```
