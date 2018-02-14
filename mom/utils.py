import random
import string
from flask import request
from datetime import datetime, timedelta
import time
import pytz


class Utils:
    @staticmethod
    def generate_random_string(size=32):
        return ''.join([random.choice(string.ascii_letters + string.digits) for x in range(size)])

    @staticmethod
    def get_client_ip():
        forwarded = request.headers.get('X-Forwarded-For')
        if forwarded is None:
            return request.remote_addr
        else:
            return forwarded

    @staticmethod
    def seconds_time_format(sec):
        now = int(time.time())
        uptimeSec = now - sec
        mins, secs = divmod(uptimeSec, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        uptime = '%2d days, %02dh %02dm %02ds' % (days, hours, mins, secs)
        return uptime
