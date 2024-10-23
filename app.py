from flask import Flask, render_template, request
from googleapiclient.discovery import build


app = Flask(__name__)

def youtube_search(query):
    api_key = 'replace_with_your_api-key'  # Replace with your actual API key
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=10
    )
    response = request.execute()

    video_ids = [item['id']['videoId'] for item in response['items']]

    video_request = youtube.videos().list(
        part="snippet,statistics",
        id=','.join(video_ids)
    )
    video_response = video_request.execute()

    videos = [
        {
            'title': video['snippet']['title'],
            'likes': video['statistics'].get('likeCount', '0'),
            'video_id': video['id'],
            'thumbnail': video['snippet']['thumbnails']['high']['url']
        }
        for video in video_response['items']
        if 'likeCount' in video['statistics']
    ]

    videos = sorted(videos, key=lambda x: int(x['likes']), reverse=True)

    return videos[:10]

@app.route('/', methods=['GET', 'POST']) 
def index():
    videos = []
    if request.method == 'POST':
        query = request.form['query']
        videos = youtube_search(query)
    return render_template('index.html', videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
