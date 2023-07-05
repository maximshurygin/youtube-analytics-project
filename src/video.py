from .utils import youtube


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            self.title = video_response['items'][0]['snippet']['title']
            self.video_url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.view_count = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except Exception:
            self.title = None
            self.video_url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """возвращает информацию для пользователя"""
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
