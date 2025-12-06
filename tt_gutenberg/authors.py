from tt_gutenberg.utils import load_gutenberg_data

def load_merged_gutenberg_data():
    """Load and return merged Gutenberg datasets."""
    return load_gutenberg_data()

def list_authors(by_languages=True, alias=True):
    """Get author information from merged Gutenberg data."""
    df_merged = load_gutenberg_data()
    
    # Drop rows where alias is missing
    if 'alias' in df_merged.columns:
        df_merged = df_merged.dropna(subset=["alias"])
    
    # Create alias count column
    if 'aliases' in df_merged.columns:
        df_merged["alias_count"] = df_merged["aliases"].fillna("").apply(
            lambda x: len(str(x).split("/")) if x else 0
        )
        df_sorted = df_merged.sort_values("alias_count", ascending=False)
    else:
        df_sorted = df_merged
    
    if alias:
        return df_sorted["alias"].tolist()
    else:
        return df_sorted