from mongoengine import Document
from mongoengine.fields import StringField


class Department(Document):
    meta = {'collection': 'department'}
    name = StringField()
