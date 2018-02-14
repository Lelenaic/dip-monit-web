from flask import Flask, request, abort, render_template
import mom
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/blank')
def blank():
    return render_template('gabarit.html')


@app.route('/create')
def create():
    s = mom.Server(ip='127.0.0.1', name='Local Server')
    s.save()
    return s.installKey


@app.route('/api/register')
def register():
    key = request.args.get('key')
    if key is not None:
        ip = mom.Utils.get_client_ip()
        s = mom.Server.get(mom.Server.installKey == key)
        if s.ip == ip and s.installed is False:
            s.installed = True
            s.save()
            return s.apiKey
    abort(401)


@app.route('/api/ping', methods=['POST'])
def ping():
    c = mom.controllers.InfoController(request)
    c.store()
    return '', 204


@app.route('/server/<int:server_id>')
def server(server_id=1):
    dataInfo = mom.Info.select().where(mom.Info.server == server_id)
    return render_template('server.html', dataInfo=dataInfo)

@app.route('/servers')
def index():
    c = mom.controllers.ServerController(request)
    return c.index()


@app.context_processor
def get_page_name():
    page_name = request.path.split('/')[1]

    def str_to_json(str):
        return json.loads(str)

    server_list = mom.Server.select()
    return dict(page_name=page_name, str_to_json=str_to_json, server_list=server_list)

if __name__ == '__main__':
    app.run(debug=True)
