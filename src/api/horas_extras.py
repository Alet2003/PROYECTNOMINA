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
from Model.horas_extras import HorasExtras, HorasExtrasSchema
routes_HorasExtras = Blueprint("routes_HorasExtras", __name__)

# usuario
HorasExtra_Schema = HorasExtrasSchema()
HorasExtras_Schema = HorasExtrasSchema(many=True)

@routes_HorasExtras.route("/HorasExtras", methods=["GET"])
def HorasExtras():
    returnall = HorasExtras.query.all()
    resultado_HorasExtras = HorasExtrasSchema.dump(returnall)
    return jsonify(resultado_HorasExtras)


@routes_HorasExtras.route("/eliminar_HorasExtras/<IDRegistroHorasExtras>", methods=["GET"])
def eliminar_HistorialPagos(IDRegistroHorasExtras):
    IDRegistroHorasExtras = HorasExtras.query.get(IDRegistroHorasExtras)
    db.session.delete(IDRegistroHorasExtras)
    db.session.commit()
    return jsonify(HorasExtrasSchema.dump(IDRegistroHorasExtras))


@routes_HorasExtras.route("/actualizarHorasExtras", methods=["POST"])
def actualizarHistorialPagos():
    IDRegistroHorasExtras = request.json["IDRegistroHorasExtras"]
    FechaRegistro = request.json["FechaRegistro"]
    HoraInicioHorasExtras = request.json["HoraInicioHorasExtras"]
    HoraFinHorasExtras = request.json["HoraFinHorasExtras"]
    TotalHorasExtras = request.json["TotalHorasExtras"]
    IDEmpleado = request.json["IDEmpleado"]
    HorasExtras = HorasExtras.query.get(IDRegistroHorasExtras)
    HorasExtras.FechaRegistro = FechaRegistro
    HorasExtras.HoraInicioHorasExtras = HoraInicioHorasExtras
    HorasExtras.HoraFinHorasExtras = HoraFinHorasExtras
    HorasExtras.TotalHorasExtras = TotalHorasExtras
    HorasExtras.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/HorasExtras")


@routes_HorasExtras.route("/save_HorasExtras", methods=["POST"])
def save_Descuentos():
    HorasExtras = request.json[
        "IDRegistroHorasExtras,  FechaRegistro, HoraInicioHorasExtras, HoraFinHorasExtras, TotalHorasExtras,IDEmpleado"
    ]
    print(HorasExtras)
    new_HistorialPagos = HorasExtras(HorasExtras)
    db.session.add(new_HistorialPagos)
    db.session.commit()
    return redirect("/HorasExtras")
