from mom.info import Info
from mom.middlewares import AuthMiddleware
from json import loads, dumps


class InfoController:
    def __init__(self, request):
        self._r = request
        self._srv = AuthMiddleware.impose(request)

    def store(self):
        data = loads(self._r.form['info'])
        info = Info(server=self._srv, memory=dumps(data['memory']), disks=dumps(data['disks']), process=dumps(data['process']), cpu=data['cpu'], uptime=data['uptime'], network=dumps(data['network']))
        info.save()
