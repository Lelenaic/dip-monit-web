from basemodel import BaseModel
from peewee import *
from server import Server
import time


class Info(BaseModel):
    server = ForeignKeyField(Server, backref="emitter")
    memory = TextField()
    disks = TextField()
    cpu = DecimalField(max_digits=3, decimal_places=1)
    tstamp = IntegerField()

    def __init__(self, *args, **kwargs):
        super(Info, self).__init__(*args, **kwargs)
        if not self.tstamp:
            self.tstamp = int(time.time())