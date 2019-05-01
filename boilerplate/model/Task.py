from datetime import datetime
from mongoengine import EmbeddedDocument
from mongoengine import DateTimeField, StringField


class Task(EmbeddedDocument):

    name = StringField()
    deadline = DateTimeField(default=datetime.now())
