from flask import render_template
from mom.inforepository import InfoRepository

class ServerController:
    def __init__(self, request):
        self._r = request

    def index(self):
        return render_template('servers.html', alive=InfoRepository)
