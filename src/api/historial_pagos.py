from common.Toke import *
from config.db import db, app, ma
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
from sqlalchemy import func, extract, distinct
from datetime import datetime

from Model.historial_pagos import HistorialPagos, HistorialPagosSchema
routes_historialpagos = Blueprint("routes_historialpagos", __name__)
now = datetime.now()

# usuario
HistorialPago_Schema = HistorialPagosSchema()
HistorialPagosSchema = HistorialPagosSchema(many=True)

@routes_historialpagos.route("/HistorialPagos", methods=["GET"])
def historialPago():
    returnall = HistorialPagos.query.all()
    resultado_HistorialPagos = HistorialPagosSchema.dump(returnall)
    return jsonify(resultado_HistorialPagos)


@routes_historialpagos.route("/eliminar_HistorialPagos/<IDRegistro>", methods=["GET"])
def eliminar_HistorialPagos(IDRegistro):
    IDRegistros = HistorialPagos.query.get(IDRegistro)
    db.session.delete(IDRegistros)
    db.session.commit()
    return jsonify(HistorialPago_Schema.dump(IDRegistros))


@routes_historialpagos.route("/actualizarHistorialPagos", methods=["POST"])
def actualizarHistorialPagos():
    IDRegistro = request.json["IDRegistro"]
    FechaPago = request.json["FechaPago"]
    TipoPago = request.json["TipoPago"]
    MontoPago = request.json["MontoPago"]
    IDEmpleado = request.json["IDEmpleado"]
    HistorialPagos = HistorialPagos.query.get(IDRegistro)
    HistorialPagos.FechaPago = FechaPago
    HistorialPagos.TipoPago = TipoPago
    HistorialPagos.MontoPago = MontoPago
    HistorialPagos.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/HistorialPagos")


@routes_historialpagos.route("/save_HistorialPagos", methods=["POST"])
def save_Descuentos():
    FechaPago = now
    TipoPago = request.json['TipoPago']
    MontoPago = request.json['MontoPago']
    IDEmpleado = request.json['IDEmpleado']
    new_HistorialPagos = HistorialPagos(FechaPago, TipoPago, MontoPago, IDEmpleado)
    print(new_HistorialPagos)
    db.session.add(new_HistorialPagos)
    db.session.commit()
    return ""
