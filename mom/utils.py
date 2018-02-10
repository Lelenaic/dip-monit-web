import random
import string


class Utils:
    @staticmethod
    def generate_random_string(size=32):
        return ''.join([random.choice(string.ascii_letters + string.digits) for x in range(size)])
