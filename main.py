from flask import Flask, request, abort, render_template
import mom
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    c = mom.controllers.ServerController(request)
    return c.index()



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

@app.route('/api/servers', methods=['GET'])
def api_servers():
    server_id = request.args.get('server_id')
    dataInfo = mom.Info.select().where(mom.Info.server == server_id).order_by(mom.Info.id.desc()).get()
    return str(dataInfo.cpu)

@app.route('/servers/<int:server_id>')
def servers(server_id=1):
    server = mom.Server.select().where(mom.Server.id == server_id)
    if len(server) == 0:
        error = 'The server you are looking for was <strong>not found</strong>.'
        return render_template('error.html', error=error, code=404, install_key=None) # No server with this ID
    server_installed = mom.Server.select().where(mom.Server.id == server_id).where(mom.Server.installed == 1)
    if len(server_installed) == 0:
        error = 'The server you are looking for is <strong>not installed</strong> yet.'
        return render_template('error.html', error=error, code=400, install_key=server[0].installKey) # Server is not installed

    dataInfo = mom.Info.select().where(mom.Info.server == server_id)
    return render_template('server_details.html', dataInfo=dataInfo, server_id=server_id)

@app.route('/servers', methods=['POST'])
def store():
    c = mom.controllers.ServerController(request)
    return c.store()


@app.context_processor
def get_page_name():
    page_name = request.path.split('/')[1]

    def str_to_json(str):
        return json.loads(str)

    server_list = mom.Server.select()
    return dict(page_name=page_name, str_to_json=str_to_json, server_list=server_list)


if __name__ == '__main__':
    app.run(debug=True)
