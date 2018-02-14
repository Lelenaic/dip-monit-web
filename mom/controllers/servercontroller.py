from flask import render_template
from mom.inforepository import InfoRepository
from mom.server import Server
from flask import jsonify


class ServerController:
    def __init__(self, request):
        self._r = request

    def index(self):
        return render_template('servers.html', alive=InfoRepository)

    def store(self):
        try:
            Server.get(Server.name == self._r.form.get('name'))
            return jsonify({'success': False})
        except:
            pass
        s = Server(ip=self._r.form.get('ip'), name=self._r.form.get('name'))
        s.save()
        return jsonify({'success': True, 'key': s.installKey})
