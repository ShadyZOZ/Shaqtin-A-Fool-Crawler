from mongoengine import BooleanField, URLField, Document


class VideoUrl(Document):
    url = URLField(unique=True, required=True)
    uploaded = BooleanField(default=False)
    video_url = URLField(required=False)
