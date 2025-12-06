import pandas as pd

def load_gutenberg_data():
    """Load all three Gutenberg datasets and merge them on author ID."""
    base_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/"
    
    authors = pd.read_csv(base_url + "gutenberg_authors.csv")
    languages = pd.read_csv(base_url + "gutenberg_languages.csv")
    metadata = pd.read_csv(base_url + "gutenberg_metadata.csv")

    # Merge metadata with authors to link author info
    merged = metadata.merge(authors, left_on="gutenberg_author_id", right_on="gutenberg_author_id", how="left")

    # Merge languages to get full language name info
    merged = merged.merge(languages, left_on="language", right_on="language", how="left")

    return merged
