from info import Info
from peewee import fn
import time


class InfoRepository:
    @staticmethod
    def get_last_timestamp_from_server(server):
        try:
            return Info().select().where(Info.server == server).order_by(Info.id.desc()).get().tstamp
        except:
            return None

    @staticmethod
    def is_alive(server):
        """
        If the last server ping is more than 10 minutes ago, considering it as dead.
        """
        if server.installed is False:
            return 2
        last_info = InfoRepository.get_last_timestamp_from_server(server)
        if last_info is None:
            return 0
        now = int(time.time())
        if now - last_info < 600:
            return 1
        else:
            return 0
