from .utils import youtube, get_video_duration, get_playlist_name, get_playlist_items
from datetime import timedelta


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = get_playlist_name(playlist_id)
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'

    @property
    def total_duration(self):
        """возвращает длительность плейлиста"""
        playlist_items = get_playlist_items(self.playlist_id)
        total_duration = sum([get_video_duration(video_id) for video_id in playlist_items], timedelta())
        return total_duration

    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        playlist_items = get_playlist_items(self.playlist_id)

        best_video_id = None
        best_likes = -1

        for video_id in playlist_items:

            video_response = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            likes = int(video_response['items'][0]['statistics']['likeCount'])
            if likes > best_likes:
                best_likes = likes
                best_video_id = video_id

        return f'https://youtu.be/{best_video_id}'
