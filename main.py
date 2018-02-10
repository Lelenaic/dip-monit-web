from flask import Flask, request
import mom

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create')
def create():
    s = mom.Server(ip='127.0.0.1')
    s.save()
    return s.installKey


@app.route('/api/register')
def register():
    key = request.args.get('key')
    if key is not None:
        s = mom.Server.get(mom.Server.installKey == key)
        return s.apiKey


if __name__ == '__main__':
    app.run()
