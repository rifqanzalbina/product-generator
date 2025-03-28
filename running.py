from productgen.ai_generator import AIProductGenerator
from productgen.generator import Style
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def format_names(names):
    """Format list of names into clean strings"""
    return names  # No need for additional formatting now

def main():
    # Initialize rich console for better formatting
    console = Console()
    generator = AIProductGenerator()

    console.print("\n[bold blue]Product Name Generator[/bold blue]")
    console.print("=" * 50)

    # Generate creative names
    names = generator.generative_creative_names(
        category="smartphone",
        brand="JojoPhone",
        style=Style.TITLE_CASE,
    )
    
    # Create table for generated names
    name_table = Table(title="Generated Product Names")
    name_table.add_column("No.", style="cyan")
    name_table.add_column("Name", style="green")
    
    for idx, name in enumerate(format_names(names), 1):
        name_table.add_row(str(idx), name)
    
    console.print(name_table)

    # Generate and display product story
    story = generator.generate_product_story("JojoPhone UltraPhone")
    console.print(Panel(story, title="Product Story", border_style="blue"))

    # Generate and display features
    features = generator.generate_product_features(
        product_name="JojoPhone UltraPhone",
        category="smartphone"
    )
    
    feature_table = Table(title="Product Features")
    feature_table.add_column("No.", style="cyan")
    feature_table.add_column("Feature", style="green")
    
    for idx, feature in enumerate(features, 1):
        feature_table.add_row(str(idx), feature)
    
    console.print(feature_table)

    # Display name analysis
    analysis = generator.analyze_name_effectiveness("JojoPhone UltraPhone")
    
    analysis_table = Table(title="Name Analysis")
    analysis_table.add_column("Metric", style="cyan")
    analysis_table.add_column("Score", style="green")
    
    for metric, score in analysis.items():
        analysis_table.add_row(metric.replace('_', ' ').title(), f"{score:.2f}")
    
    console.print(analysis_table)

    # Batch generate names
    categories = ["smartphone", "laptop", "tablet"]
    batch_result = generator.batch_generate_names(categories, brand="JojoPhone")
    
    console.print("\n[bold blue]Batch Generated Names[/bold blue]")
    
    for category, names in batch_result.items():
        batch_table = Table(title=f"{category.title()} Names")
        batch_table.add_column("No.", style="cyan")
        batch_table.add_column("Name", style="green")
        
        for idx, name in enumerate(format_names(names), 1):
            batch_table.add_row(str(idx), name)
        
        console.print(batch_table)
        console.print("")

if __name__ == "__main__":
    main()