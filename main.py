from flask import Flask, request
import mom

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create')
def create():
    s = mom.Server(ip='46.105.145.239')
    s.save()
    return s.installKey


@app.route('/api/register')
def register():
    key = request.args.get('key')
    if key is not None:
        s = mom.Server.get(mom.Server.installKey == key)
        if s.ip == request.remote_addr and s.installed is False:
            s.installed = True
            s.save()
            return s.apiKey
    return ''


@app.route('/api/ping', methods=['POST'])
def ping():
    c = mom.controllers.InfoController(request)
    c.store()
    return '', 204


@app.route('/info')
def info():
    i = mom.Info.select(mom.Server.id == 1).count()
    return str(i)


if __name__ == '__main__':
    app.run()
