from basemodel import BaseModel
from peewee import *
from server import Server
import time
from utils import Utils


class Info(BaseModel):
    server = ForeignKeyField(Server, backref="emitter")
    memory = TextField()
    disks = TextField()
    process = TextField()
    network = TextField()
    cpu = DecimalField(max_digits=3, decimal_places=1)
    uptime = IntegerField()
    tstamp = IntegerField()

    def __init__(self, *args, **kwargs):
        super(Info, self).__init__(*args, **kwargs)
        if not self.tstamp:
            self.tstamp = int(time.time())

    def get_formatted_time(self):
        return Utils.seconds_time_format(self.uptime)
