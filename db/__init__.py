from mongoengine import connect

from .settings import DB, PORT
from .documents import VideoUrl

connect(DB, port=PORT)

__all__ = [
    'VideoUrl',
]
