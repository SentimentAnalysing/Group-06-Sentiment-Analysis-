import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon', quiet=True)


def label_with_vader(comment, analyzer):
    sentiment = analyzer.polarity_scores(comment)
    if sentiment['compound'] >= 0.05:
        return "positive"
    elif sentiment['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"


def label_comments_vader(input_filepath, output_filepath):

    analyzer = SentimentIntensityAnalyzer()
    df = pd.read_csv(input_filepath)
    if "Comment" not in df.columns:
        print("Error: 'Comment' column not found in the file.")
        return None  
    
    df["Sentiment"] = df["Comment"].apply(lambda x: label_with_vader(x, analyzer))
    df.to_csv(output_filepath, index=False)
    print(f"Sentiments labeled and saved to: {output_filepath}")
    return df  # بازگشت دیتافریم



