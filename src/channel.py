from .utils import youtube, printj
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        snippet = self.channel_info['items'][0]['snippet']
        statistics = self.channel_info['items'][0]['statistics']

        self.title = snippet['title']
        self.description = snippet['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(statistics['subscriberCount'])
        self.video_count = int(statistics['videoCount'])
        self.view_count = int(statistics['viewCount'])

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """класс-метод, возвращающий объект для работы с YouTube API"""
        return youtube

    def to_json(self, filename):
        """метод, сохраняющий в файл значения атрибутов экземпляра `Channel`"""

        channel_data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_data, file)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        printj(self.channel_info)
