from textblob import TextBlob
import pandas as pd

def label_negative_sentiment(comment):
    sentiment = TextBlob(comment).sentiment.polarity
    return sentiment < 0 

def filter_negative_comments(comments_list):
    df = pd.DataFrame(comments_list, columns=["Comment"])
    
    df["Is_Negative"] = df["Comment"].apply(label_negative_sentiment)
    negative_comments = df[df["Is_Negative"]]
    
    return negative_comments
