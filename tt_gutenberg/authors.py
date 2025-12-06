import pandas as pd
from tt_gutenberg.utils import load_gutenberg_data


def list_authors(by_languages=True, alias=True):
    base_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/"
    
    df_authors = pd.read_csv(base_url + "gutenberg_authors.csv")
    df_metadata = pd.read_csv(base_url + "gutenberg_metadata.csv")
    df_languages = pd.read_csv(base_url + "gutenberg_languages.csv")
    
    df_merged = pd.merge(df_authors, df_metadata, on='gutenberg_id', how='inner')
    
    df_merged = pd.merge(df_merged, df_languages, on='gutenberg_id', how='inner')
    
    df_merged = df_merged.dropna(subset=["alias"])
    
    df_merged["alias_count"] = df_merged["aliases"].fillna("").apply(
        lambda x: len(str(x).split("/"))
    )
    
    df_sorted = df_merged.sort_values("alias_count", ascending=False)
    
    if alias:
        return df_sorted["alias"].tolist()
    else:
        return df_sorted
