from datetime import datetime, timedelta
from os import name

from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'


@app.route('/login')
def login():
    auth = request.authorization()

    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(minutes=30)},
                           app.config['SECRET_KEY'])

        return jsonify({'token': token()})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/protected')
def protection():
    token = request.args.get('token')
    return '''<h1> The token is {} <h1>'''.format(token)


if __name__ == 'main':
    app.run(debug=True)
