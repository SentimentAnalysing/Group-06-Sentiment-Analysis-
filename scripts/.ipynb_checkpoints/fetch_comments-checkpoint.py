from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv
import os

#loading .env file
load_dotenv()
API_KEY = os.getenv("API_KEY");
print(f"Your API Key is: {API_KEY}")
youtube = build('youtube', 'v3', developerKey=API_KEY)


#fetching the comments
def fetch_comments(video_id, max_results=1000):
    comments = []
    next_page_token = None
    fetched_comments = 0

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=1000,
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
            fetched_comments += 1

        next_page_token = response.get("nextPageToken")
        if not next_page_token or len(comments) >= max_results:
            break

    return comments



#saving comments to csv files
def save_to_csv(comments, filename):
    df = pd.DataFrame(comments, columns=["Comment"])
    df.to_csv(filename, index=False)
    print(f"Saved {len(comments)} comments to {filename}")

if __name__ == "__main__":
    video_id = "JfVOs4VSpmA"  
    comments = fetch_comments(video_id, max_results=1000)
    save_to_csv(comments, "{output_dir}/comments.csv")