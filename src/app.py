
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma
from common.Toke import *
from Model import *

from rutas.home import routes_home

# from api.roles import routes_roles

# app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_home, url_prefix="/fronted")


#------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template('/index.html')

# @app.route("/algo")
# def otr():
#     return render_template('/main/homeodontologo.html',)

# @app.route('/indexagendarcitas', methods=['GET'] )
# def indexhome():
#     return render_template('/main/agendarcitas.html')

if __name__ == '__main__':

    app.run(debug=True, port=5000, host='0.0.0.0')
    