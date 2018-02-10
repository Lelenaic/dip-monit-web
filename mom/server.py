from basemodel import BaseModel
from peewee import *
from utils import Utils


class Server(BaseModel):
    ip = CharField()
    installKey = CharField(max_length=12)
    apiKey = CharField(max_length=128)
    installed = BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(Server, self).__init__(*args, **kwargs)
        self._generate_api_key()
        self._generate_install_key()

    def _generate_api_key(self):
        if self.apiKey is None:
            self.apiKey = Utils.generate_random_string(128)

    def _generate_install_key(self):
        if self.installKey is None:
            self.installKey = Utils.generate_random_string(12)
