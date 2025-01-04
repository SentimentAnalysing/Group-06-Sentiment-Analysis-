from textblob import TextBlob
import pandas as pd

def label_neutral_sentiment(comment):
    sentiment = TextBlob(comment).sentiment.polarity
    return sentiment == 0 

def filter_neutral_comments(comments_list):
    df = pd.DataFrame(comments_list, columns=["Comment"])
    
    df["Is_Neutral"] = df["Comment"].apply(label_neutral_sentiment)
    neutral_comments = df[df["Is_Neutral"]]
    
    return neutral_comments
