import json
import os
from datetime import timedelta

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


def get_video_duration(video_id):
    """Вовзращает длительность видео по его id"""
    video_response = youtube.videos().list(
        part='contentDetails',
        id=video_id
    ).execute()

    duration_str = video_response['items'][0]['contentDetails']['duration']
    duration = timedelta()
    value = 0

    for char in duration_str:
        if char.isdigit():
            value = value * 10 + int(char)
        else:
            if char == 'H':
                duration += timedelta(hours=value)
            elif char == 'M':
                duration += timedelta(minutes=value)
            elif char == 'S':
                duration += timedelta(seconds=value)

            value = 0

    return duration


def get_playlist_name(playlist_id):
    """возвращает имя плейлиста по его id"""
    playlist_response = youtube.playlists().list(
        part='snippet',
        id=playlist_id
    ).execute()

    playlist_name = playlist_response['items'][0]['snippet']['title']
    return playlist_name


def get_playlist_items(playlist_id):
    """возвращает список элементов плейлиста по его id"""
    playlist_items = []
    next_page_token = None

    while True:
        playlist_response = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        playlist_items.extend(item['contentDetails']['videoId'] for item in playlist_response['items'])

        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break

    return playlist_items
