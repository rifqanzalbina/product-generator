# product generator

<img src="https://github.com/user-attachments/assets/14837acb-b116-4a80-b158-2ebbc1c500b2" width="300" alt="PRoduct (1)">

## Install

```python
pip install productgen
```

## Key Modules & Features

### AIProductGenerator
- **generative_creative_names(category, brand, num_suggestions)**  
  Generates creative product name suggestions by leveraging a language model (e.g. GPT-2).  
- **generate_product_story(product_name)**  
  Produces a short, compelling story or description for the given product.  

### Generator Module
- **generate_product_name**  
  Combines category, subcategory, brand, and style (e.g. hyphenation, title casing) to form product names.  
- **generate_marketing_taglines**  
  Returns sample taglines for marketing, incorporating style or suffix.  

### Analyzer (ProductNameAnalyzer)
- **analyze_sentiment**  
  Calculates sentiment and subjectivity for a given product name.  
- **suggest_improvements**  
  Provides suggestions for improvement if the sentiment score or memorability is low.

### ProductGenConfig
- **load_config / save_config**  
  Loads and saves configuration (e.g., custom brands) to a JSON file.  
- **add_custom_brand**  
  Adds a custom brand entry to the config, avoiding duplicates.

---

# How To Usage ?

## 1. Via example.py
```py
# file: example_usage.py
from productgen.generator import generate_product_name, Style

def main():
    product_1 = generate_product_name(Style.SIMPLE_CONCAT)
    print("Contoh nama produk:", product_1)

    product_2 = generate_product_name(Style.TITLE_CASE, brand="MyBrand", use_suffix=True, use_tagline=True)
    print("Contoh nama produk dengan brand, suffix, dan tagline:", product_2)

if __name__ == "__main__":
    main()
```
Run it:
```bash
python example.py
```

## 2. Via running.py
```py
# file: running.py
from productgen.ai_generator import AIProductGenerator
from productgen.generator import Style
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def format_names(names):
    return names

def main():
    console = Console()
    generator = AIProductGenerator()

    console.print("[bold blue]Product Name Generator[/bold blue]")
    console.print("=" * 50)

    # Generate creative names
    names = generator.generative_creative_names(
        category="smartphone",
        brand="JojoPhone",
        style=Style.TITLE_CASE,
    )

    # Display in a table
    name_table = Table(title="Generated Product Names")
    name_table.add_column("No.", style="cyan")
    name_table.add_column("Name", style="green")
    
    for idx, name in enumerate(format_names(names), 1):
        name_table.add_row(str(idx), name)
    console.print(name_table)

    # Generate product story
    story = generator.generate_product_story("JojoPhone UltraPhone")
    console.print(Panel(story, title="Product Story", border_style="blue"))

    # Generate features
    features = generator.generate_product_features("JojoPhone UltraPhone", "smartphone")
    feature_table = Table(title="Product Features")
    feature_table.add_column("No.", style="cyan")
    feature_table.add_column("Feature", style="green")
    for i, f in enumerate(features, 1):
        feature_table.add_row(str(i), f)
    console.print(feature_table)

    # Analyze the name
    analysis = generator.analyze_name_effectiveness("JojoPhone UltraPhone")
    analysis_table = Table(title="Name Analysis")
    analysis_table.add_column("Metric", style="cyan")
    analysis_table.add_column("Score", style="green")
    for metric, score in analysis.items():
        analysis_table.add_row(metric, f"{score:.2f}")
    console.print(analysis_table)

    # Batch generate names
    categories = ["smartphone", "laptop", "tablet"]
    batch_result = generator.batch_generate_names(categories, brand="JojoPhone")
    console.print("[bold blue]Batch Generated Names[/bold blue]")
    for category, generated_names in batch_result.items():
        cat_table = Table(title=f"{category.title()} Names")
        cat_table.add_column("No.", style="cyan")
        cat_table.add_column("Name", style="green")
        for idx, nm in enumerate(format_names(generated_names), 1):
            cat_table.add_row(str(idx), nm)
        console.print(cat_table)
        console.print("")

if __name__ == "__main__":
    main()
```
Run it:
```bash
python running.py
```
