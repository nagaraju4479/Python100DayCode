from googleapiclient.discovery import build
import re

api_key = 'AIzaSyAdOZ0QrLhpRrM-kEttpfOySKHDzPi4494'
youtube = build('youtube', 'v3', developerKey=api_key)

videos_response = youtube.search().list(
    part='snippet',
    type='video',
    videoCategoryId='10', # category ID for Gaming
    order='viewCount', # order by view count
    maxResults=50
    
).execute()
hashtags = []
for video in videos_response['items']:
    title = video['snippet']['title']
    description = video['snippet']['description']
    combined = title + ' ' + description
    matches = re.findall(r'#(\w+)', combined)
    hashtags += matches

# hashtag_counts = {tag: hashtags.count(tag) for tag in set(hashtags)}
# print(f'{hashtags} and {hashtag_counts} \n')
print(f"{hashtags}\n")