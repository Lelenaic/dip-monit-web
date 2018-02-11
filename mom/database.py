from peewee import *
from consts import Consts
from settings import _Settings

s = _Settings()

db_type = s.get('database', 'type')

if db_type == 'sqlite':
    db = SqliteDatabase(Consts.MOM_SQLITE_FILE)
elif db_type == 'mysql':
    database_name = s.get('database', 'name')
    database_ip = s.get('database', 'host')
    database_username = s.get('database', 'user')
    database_password = s.get('database', 'pass')
    db = MySQLDatabase(None)
    db.init(database_name, host=database_ip, user=database_username, password=database_password)
else:
    raise Exception(
        'Invalid database settings. Available drivers are sqlite or mysql. Please correct your settings.yaml file.'
    )

try:
    db.connect(True)
except:
    pass
