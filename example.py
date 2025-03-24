from productgen.generator import generate_product_name, Style

def main():
    product_1 = generate_product_name(Style.SIMPLE_CONCAT)
    print("Contoh nama produk:", product_1)

    product_2 = generate_product_name(Style.TITLE_CASE, brand="MyBrand", use_suffix=True, use_tagline=True)
    print("Contoh nama produk dengan brand, suffix, dan tagline:", product_2)

if __name__ == "__main__":
    main()