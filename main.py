from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\admin\Documents\Database1.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")



except pyodbc.Error as e:
    print("Error in Connection", e)

@app.route('/login')
def login():
    auth = request.authorization
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(`id`) from user')
    a = cursor.fetchall()[0][0]
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.utcnow() + timedelta(minutes=30)},
                           app.config['SECRET_KEY'])
        myuser = (
            (a + 1, auth.username, auth.password, token),
        )
        cursor.executemany('INSERT INTO user VALUES (?,?,?,?)', myuser)
        conn.commit()
        return jsonify({'token': token})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/protected')
def protection():
    token = request.args.get('token')
    cursor = conn.cursor()
    cursor.execute('SELECT  token from user')
    for row in cursor.fetchall():
        TOKEN = row[0]
    conn.commit()
    if token == TOKEN:
        return '''<h1> The token is {} <h1>'''.format(token)
    return '''<h1> This Token is wrong!!! <h1>'''

if __name__ == '__main__':
    app.run(debug=True)