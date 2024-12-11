from textblob import TextBlob
import pandas as pd

def label(comment):
    sentiment = TextBlob(comment).sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"
        
#load csv
def label_comments(input_filepath):
    df = pd.read_csv(input_filepath)
    df["Sentiment"] = df["Comment"].apply(label)
    print(df[["Comment", "Sentiment"]].head())

    return df