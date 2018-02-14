import random
import string
from flask import request
import datetime


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
        ''' @TODO Format the number of seconds in 'sec' to auto format with days hours minutes (no seconds) '''
        return sec
