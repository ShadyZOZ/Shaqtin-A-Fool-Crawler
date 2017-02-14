from mongoengine import BooleanField, URLField, Document, StringField


class VideoUrl(Document):
    url = URLField(unique=True, required=True)
    uploaded = BooleanField(default=False)
    name = StringField(required=False)
