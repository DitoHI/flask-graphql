from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    DateTimeField,
    ReferenceField,
    ListField,
    EmbeddedDocumentField,
)
from .Department import Department
from .Role import Role
from .Task import Task


class Employee(Document):
    meta = {"collection": "employee"}
    name = StringField()
    hired_on = DateTimeField(default=datetime.now())
    department = ReferenceField(Department)
    roles = ListField(ReferenceField(Role))
    leader = ReferenceField("Employee")
    tasks = ListField(EmbeddedDocumentField(Task))
