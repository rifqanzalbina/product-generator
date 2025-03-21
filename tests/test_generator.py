import unittest
from product_generator import generate_product_name, Style

class TestProductNameGenerator(unittest.TestCase):
    def test_generate_product_name(self):
        # Test simple concatenation style
        name = generate_product_name(Style.SIMPLE_CONCAT)
        print(f"Generated name: {name}")
        print(f"Length of name: {len(name.split())}")
        self.assertTrue(len(name.split()) == 2)

        # Test hyphenation style
        name = generate_product_name(Style.HYPHENATION)
        self.assertTrue(len(name.split()) == 1)
        self.assertTrue('-' in name)

        # Test title case style
        name = generate_product_name(Style.TITLE_CASE)
        self.assertTrue(name.istitle())

        # Test capitalization style
        name = generate_product_name(Style.CAPITALIZATION)
        self.assertTrue(name.isupper())

        # Test random capitalization style
        name = generate_product_name(Style.RANDOM_CAPITALIZATION)
        self.assertTrue(name[0].isupper() or name[0].islower())
        self.assertTrue(name[1:].isupper() or name[1:].islower())

        # Test random word order style
        name = generate_product_name(Style.RANDOM_WORD_ORDER)
        self.assertTrue(len(name.split()) == 2)
        self.assertNotEqual(name.split()[0], generate_product_name(Style.RANDOM_WORD_ORDER).split()[0])

if __name__ == '__main__':
    unittest.main()