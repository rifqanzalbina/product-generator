import sys
import os

# Make sure Python can find the `productgen` package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from productgen.ai_generator import AIProductGenerator

if __name__ == "__main__":
    generator = AIProductGenerator()

    # Test creative product names
    names = generator.generative_creative_names("shoes", "Longity")
    print("Generated Names:")
    print(names)

    # Test product story
    story = generator.generate_product_story("Awesome Shoe")
    print("\nGenerated Story:")
    print(story)