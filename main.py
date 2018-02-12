from flask import Flask, request, abort, render_template
import mom

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/blank/')
def blank():
    return render_template('gabarit.html')


@app.route('/create/')
def create():
    s = mom.Server(ip='127.0.0.1')
    s.save()
    return s.installKey


@app.route('/api/register/')
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


@app.route('/api/ping/', methods=['POST'])
def ping():
    c = mom.controllers.InfoController(request)
    c.store()
    return '', 204


@app.route('/info/')
def info():
    i = mom.Info.select(mom.Server.id == 1).count()
    return str(i)


@app.context_processor
def get_page_name():
    page_name = request.path[1:-1]
    return dict(page_name=page_name)

if __name__ == '__main__':
    app.run(debug=True)
