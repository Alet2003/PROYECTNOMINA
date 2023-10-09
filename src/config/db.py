from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pymysql

app = Flask(__name__)

pymysql.install_as_MySQLdb()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/dbnomina'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "dbnomina"

db = SQLAlchemy(app)

ma = Marshmallow(app)