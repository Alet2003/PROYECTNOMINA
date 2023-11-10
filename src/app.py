#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma
from common.Toke import *


from api.empleados import routes_empleados
from api.descuentos import routes_Descuentos
from api.creditos import routes_Creditos
from api.deducciones import routes_Deducciones
from api.historial_pagos import routes_historialpagos
from api.horas_extras import routes_HorasExtras
from api.pagos import routes_Pagos
from api.registro_horas_trabajadas import routes_RegistroHorasTrabajadas
from api.vacaciones_tiempo_libre  import routes_VacacionesTiempoLibre

from rutas.home import routes_home

app.register_blueprint(routes_empleados, url_prefix="/api")
app.register_blueprint(routes_Descuentos, url_prefix="/api")
app.register_blueprint(routes_Creditos, url_prefix="/api")
app.register_blueprint(routes_Deducciones, url_prefix="/api")
app.register_blueprint(routes_historialpagos, url_prefix="/api")
app.register_blueprint(routes_HorasExtras, url_prefix="/api")
app.register_blueprint(routes_Pagos, url_prefix="/api")
app.register_blueprint(routes_RegistroHorasTrabajadas, url_prefix="/api")
app.register_blueprint(routes_VacacionesTiempoLibre, url_prefix="/api")

#------------------------------------------------

app.register_blueprint(routes_home, url_prefix="/fronted")

#------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template('/index.html')

@app.route("/demo", methods=["GET"])
def demo():
    return render_template('/home.html')

# @app.route("/algo")
# def otr():
#     return render_template('/main/homeodontologo.html',)

# @app.route('/indexagendarcitas', methods=['GET'] )
# def indexhome():
#     return render_template('/main/agendarcitas.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
    