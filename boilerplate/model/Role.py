from mongoengine import Document
from mongoengine.fields import StringField

class Role(Document):
    meta = {'collection': 'role'}
    name = StringField()