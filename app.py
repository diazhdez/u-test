from flask import Flask, render_template

from session import session_routes

from user import user_routes

from admin import admin_routes

from functions import *

import database as dbase

db = dbase.dbConnection()

app = Flask(__name__)

app.secret_key = 'M0i1Xc$GfPw3Yz@2SbQ9lKpA5rJhDtE7'


# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')


# Registrar blueprints
app.register_blueprint(session_routes)

app.register_blueprint(admin_routes)

app.register_blueprint(user_routes)


if __name__ == '__main__':
    app.run(debug=True)
