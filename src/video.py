from .utils import youtube


class Video:
    def __init__(self, video_id):
        self.video_id = video_id

        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.video_url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """возвращает информацию для пользователя"""
        return self.video_title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
