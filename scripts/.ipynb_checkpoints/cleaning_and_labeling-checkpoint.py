import pandas as pd
from langdetect import detect
from emoji import replace_emoji

# Loading raw comments
def load_comments(input_filepath):
    try:
        df = pd.read_csv(input_filepath)
        print(f"Loaded {len(df)} comments from {input_filepath}")
        return df
    except FileNotFoundError:
        print(f"File not found: {input_filepath}")
        return None

# Remove non english 
def is_english(comment):
    try:
        return detect(comment) == "en"
    except:
        return False  

def filter_non_english_comments(df):
    print("Filtering non-English comments...")
    df["is_english"] = df["Comment"].apply(is_english)
    english_df = df[df["is_english"]].drop(columns=["is_english"])
    print(f"Kept {len(english_df)} English comments.")
    return english_df

# Remove emojis 
def has_text(comment):
    return any(c.isalnum() for c in replace_emoji(comment, ""))

def filter_emoji_only_comments(df):
    print("Removing emoji-only comments...")
    df["has_text"] = df["Comment"].apply(has_text)
    text_df = df[df["has_text"]].drop(columns=["has_text"])
    print(f"Kept {len(text_df)} comments with text.")
    return text_df

# Save filtered comments
def save_cleaned_comments(df, output_filepath):
    df.to_csv(output_filepath, index=False)
    print(f"Saved cleaned comments to {output_filepath}")

# Main
if __name__ == "__main__":
    input_filepath = "../data/new_comments.csv"
    output_filepath = "../data/cleaned_comments.csv"

    df = load_comments(input_filepath)
    if df is not None:
       
        df = filter_non_english_comments(df)

        df = filter_emoji_only_comments(df)

        save_cleaned_comments(df, output_filepath)
