import pandas as pd

def load_gutenberg_data():
    """Load all three Gutenberg datasets and merge them."""
    base_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/"
    
    print("Loading gutenberg_authors.csv...")
    authors = pd.read_csv(base_url + "gutenberg_authors.csv")
    print(f"Authors shape: {authors.shape}")
    
    print("Loading gutenberg_metadata.csv...")
    metadata = pd.read_csv(base_url + "gutenberg_metadata.csv")
    print(f"Metadata shape: {metadata.shape}")
    
    print("Loading gutenberg_languages.csv...")
    languages = pd.read_csv(base_url + "gutenberg_languages.csv")
    print(f"Languages shape: {languages.shape}")
    
    
    print("\nMerging metadata + authors...")
    merged = metadata.merge(
        authors, 
        on="gutenberg_author_id",  
        how="left",
        suffixes=('_metadata', '_author')
    )
    print(f"After merging metadata + authors: {merged.shape}")
    
   
    print("\nMerging with languages...")
    merged = merged.merge(
        languages, 
        on="gutenberg_id",  
        how="left",
        suffixes=('', '_lang')
    )
    print(f"Final merged shape: {merged.shape}")
    
    return merged