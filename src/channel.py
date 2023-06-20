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

    def __str__(self):
        """Возвращает описание для пользователя"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Возвращает сумму подписчиков такущего и другого объекта"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """Возвращает разницу подписчиков такущего и другого объекта"""
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        """
        Проверяет, является ли количество подписчиков текущего объекта меньшим, чем количество подписчиков другого
        объекта.
        Возвращает bool
        """
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        """
        Проверяет, является ли количество подписчиков текущего объекта меньшим или равным количеству подписчиков другого
        объекта.
        Возвращает bool
        """
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """
        Проверяет, является ли количество подписчиков текущего объекта большим, чем количество подписчиков другого
        объекта.
        Возвращает bool
        """
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """
        Проверяет, является ли количество подписчиков текущего объекта большим или равным количеству подписчиков другого
        объекта.
        Возвращает bool
        """
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other):
        """
        Проверяет, является ли количество подписчиков текущего объекта равным количеству подписчиков другого объекта.
        Возвращает bool
        """
        return self.subscriber_count == other.subscriber_count

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
