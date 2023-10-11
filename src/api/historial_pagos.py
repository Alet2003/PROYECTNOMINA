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
from sqlalchemy import func, extract
from Model.historial_pagos import HistorialPagos, HistorialPagosSchema
routes_historialpagos = Blueprint("routes_historialpagos", __name__)

# usuario
HistorialPago_Schema = HistorialPagosSchema()
HistorialPagosSchema = HistorialPagosSchema(many=True)

@routes_historialpagos.route("/HistorialPagos", methods=["GET"])
def HistorialPagos():
    returnall = HistorialPagos.query.all()
    resultado_HistorialPagos = HistorialPagosSchema.dump(returnall)
    return jsonify(resultado_HistorialPagos)


@routes_historialpagos.route("/eliminar_HistorialPagos/<IDRegistro>", methods=["GET"])
def eliminar_HistorialPagos(IDRegistro):
    IDRegistro = HistorialPagos.query.get(IDRegistro)
    db.session.delete(IDRegistro)
    db.session.commit()
    return jsonify(HistorialPagosSchema.dump(IDRegistro))


@routes_historialpagos.route("/actualizarHistorialPagos", methods=["POST"])
def actualizarHistorialPagos():
    IDRegistro = request.json["IDRegistro"]
    FechaAplicacionDescuento = request.json["IDDescuento"]
    TipoDescuento = request.json["TipoDescuento"]
    MontoDescuento = request.json["MontoDescuento"]
    DescripcionDescuento = request.json["DescripcionDescuento"]
    IDEmpleado = request.json["IDEmpleado"]
    HistorialPagos = HistorialPagos.query.get(IDRegistro)
    HistorialPagos.FechaAplicacionDescuento = FechaAplicacionDescuento
    HistorialPagos.TipoDescuento = TipoDescuento
    HistorialPagos.MontoDescuento = MontoDescuento
    HistorialPagos.DescripcionDescuento = DescripcionDescuento
    HistorialPagos.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/HistorialPagos")


@routes_historialpagos.route("/save_Descuentos", methods=["POST"])
def save_Descuentos():
    HistorialPagos = request.json[
        "IDDescuento, FechaAplicacionDescuento, TipoDescuento, MontoDescuento, DescripcionDescuento, IDEmpleado"
    ]
    print(HistorialPagos)
    new_Descuentos = HistorialPagos(HistorialPagos)
    db.session.add(new_Descuentos)
    db.session.commit()
    return redirect("/Descuentos")
