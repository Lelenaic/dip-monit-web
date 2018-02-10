import yaml
from consts import Consts
import os.path


class _Settings:

    def __init__(self):
        if os.path.isfile(Consts.MOM_SETTINGS_FILE):
            self._load_config_file()
        else:
            raise Exception("There is no file: " + Consts.MOM_SETTINGS_FILE)

    def _load_config_file(self):
        with open(Consts.MOM_SETTINGS_FILE, 'r') as f:
            self._conf_file = yaml.load(f)
            if self._conf_file is None:
                self._conf_file = {}

    def get(self, *setting):
        conf = self._conf_file
        for s in setting:
            conf = conf[s]
        return conf

    def set(self, **settings):
        for setting in settings:
            self._conf_file[setting] = settings[setting]
        self._save()

    def _save(self):
        with open(Consts.MOM_SETTINGS_FILE, 'w') as f:
            f.write(yaml.dump(self._conf_file))
