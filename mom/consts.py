import os


class Consts:
    MOM_HOME = os.path.dirname(os.path.abspath(__file__))[:-4]
    MOM_FILES_DIR = MOM_HOME + os.path.sep + "files" + os.path.sep
    MOM_SQLITE_FILE = MOM_FILES_DIR + "database.sqlite"
    MOM_INSTALL_LOCK_FILE = MOM_FILES_DIR + "LOCK"
    MOM_SETTINGS_FILE = MOM_FILES_DIR + os.path.sep + "settings.yaml"
