import unittest
from productgen.generator import generate_product_name, Style

class TestGenerator(unittest.TestCase):
    def test_generate_with_brand(self):
        name = generate_product_name(Style.HYPHENATION, brand="TestBrand")
        self.assertTrue(name.startswith("TestBrand"), "Gagal menggunakan brand")

    def test_generate_with_suffix(self):
        name = generate_product_name(Style.TITLE_CASE, use_suffix=True)
        self.assertRegex(name, r"\d{3}$", "Sufiks angka tidak ditemukan di akhir")

    def test_generate_with_tagline(self):
        name = generate_product_name(Style.CAPITALIZATION, use_tagline=True)
        self.assertIn("AwesomeTag", name, "Tagline tidak ditambahkan")

if __name__ == '__main__':
    unittest.main()