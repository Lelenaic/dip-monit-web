from peewee import Model
from mom.database import db


class BaseModel(Model):
    class Meta:
        database = db
