from basemodel import BaseModel
from peewee import *
from server import Server


class Info(BaseModel):
    server = ForeignKeyField(Server, backref="emitter")
    memory = TextField()
    disks = TextField()
    cpu = DecimalField(max_digits=2, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(Info, self).__init__(*args, **kwargs)
