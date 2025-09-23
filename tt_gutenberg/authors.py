import pandas as pd

def list_authors(by_languages=True, alias=True):
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    df = pd.read_csv(url)

    # Drop rows where alias is missing
    df = df.dropna(subset=["alias"])

    # Create a new column counting number of aliases (split by '/')
    df["alias_count"] = df["aliases"].fillna("").apply(lambda x: len(str(x).split("/")))

    # Sort by alias_count, highest first
    df_sorted = df.sort_values("alias_count", ascending=False)

    # Return only aliases if requested
    if alias:
        return df_sorted["alias"].tolist()
    else:
        return df_sorted[["author", "alias_count"]]
