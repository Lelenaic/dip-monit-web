from server import Server
from mom_database import db
import os
from consts import Consts

if os.path.isfile(Consts.MOM_INSTALL_LOCK_FILE):
    raise Exception('Delete the LOCK file if you want to re-install Mom.')

db.create_tables([Server])

with open(Consts.MOM_INSTALL_LOCK_FILE, 'a'):
    os.utime(Consts.MOM_INSTALL_LOCK_FILE, None)
