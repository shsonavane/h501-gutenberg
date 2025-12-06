import pandas as pd
from tt_gutenberg.utils import load_gutenberg_data

def list_authors(by_languages=True, alias=True):
    """
    Return author aliases sorted by translation count across languages.
    """
    df = load_gutenberg_data()

    # Drop missing authors
    df = df.dropna(subset=["alias"])

    # Compute translation count per author (unique languages)
    translation_counts = (
        df.groupby(["gutenberg_author_id", "alias"])["language"]
          .nunique()
          .reset_index(name="translation_count")
    )

    # Sort by translation count (descending)
    df_sorted = translation_counts.sort_values("translation_count", ascending=False)

    if alias:
        return df_sorted["alias"].tolist()
    else:
        return df_sorted.head(20)
