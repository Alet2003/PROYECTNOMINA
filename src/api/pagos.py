from common.Toke import *
from config.db import db, app, ma
from datetime import datetime
from flask import (
    Flask,
    Blueprint,
    redirect,
    request,
    jsonify,
    json,
    session,
    render_template,
)
from sqlalchemy import func, extract
from Model.pagos import Pagos, PagosSchema
routes_Pagos = Blueprint("routes_Pagos", __name__)
now = datetime.now()

# usuario
Pago_Schema = PagosSchema()
Pagos_Schema = PagosSchema(many=True)

@routes_Pagos.route("/Pagos", methods=["GET"])
def pagos():
    returnall = Pagos.query.all()
    resultado_Pagos = Pagos_Schema.dump(returnall)
    return jsonify(resultado_Pagos)

@routes_Pagos.route("/eliminar_Pagos/<IDPago>", methods=["GET"])
def eliminar_Pagos(IDPago):
    IDPago = Pagos.query.get(IDPago)
    db.session.delete(IDPago)
    db.session.commit()
    return jsonify(PagosSchema.dump(IDPago))

@routes_Pagos.route("/actualizarPagos", methods=["POST"])
def actualizarPagos():
    IDPago = request.json["IDPago"]
    FechaPago = request.json["FechaPago"]
    TipoPago = request.json["TipoPago"]
    MontoPago = request.json["MontoPago"]
    IDEmpleado = request.json["IDEmpleado"]
    Pagos = Pagos.query.get(IDPago)
    Pagos.FechaPago = FechaPago
    Pagos.TipoPago = TipoPago
    Pagos.MontoPago = MontoPago
    Pagos.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/Pagos")

@routes_Pagos.route("/save_Pagos", methods=["POST"])
def save_Pagos():
    FechaPago = now
    TipoPago = request.json['TipoPago']
    MontoPago = request.json['MontoPago']
    IDEmpleado = request.json['IDEmpleado']
    new_HistorialPagos = Pagos(FechaPago, TipoPago, MontoPago, IDEmpleado)
    print(new_HistorialPagos)
    db.session.add(new_HistorialPagos)
    db.session.commit()
    return ""