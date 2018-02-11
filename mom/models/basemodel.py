from peewee import Model
from mom.mom_database import db


class BaseModel(Model):
    class Meta:
        database = db
