from product_generator import generate_product_name, Style

# Generate a product name using the simple concatenation style
simple_concat_name = generate_product_name(Style.SIMPLE_CONCAT)
print(f"Simple Concatenation Style: {simple_concat_name}")

# Generate a product name using the hyphenation style
hyphenation_name = generate_product_name(Style.HYPHENATION)
print(f"Hyphenation Style: {hyphenation_name}")

# Generate a product name using the title case style
title_case_name = generate_product_name(Style.TITLE_CASE)
print(f"Title Case Style: {title_case_name}")

# Generate a product name using the capitalization style
capitalization_name = generate_product_name(Style.CAPITALIZATION)
print(f"Capitalization Style: {capitalization_name}")

# Generate a product name using the random capitalization style
random_capitalization_name = generate_product_name(Style.RANDOM_CAPITALIZATION)