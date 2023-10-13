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
from Model.pagos import Pagos, PagosSchema
routes_Pagos = Blueprint("routes_Pagos", __name__)

# usuario
Pago_Schema = PagosSchema()
Pagos_Schema = PagosSchema(many=True)

@routes_Pagos.route("/Pagos", methods=["GET"])
def Pagos():
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
    return redirect("/Pagos")

@routes_Pagos.route("/save_Pagos", methods=["POST"])
def save_Pagos():
    Pagos = request.json[
        "IDRegistroHorasExtras,  FechaRegistro, HoraInicioHorasExtras, HoraFinHorasExtras, TotalHorasExtras,IDEmpleado"
    ]
    print(Pagos)
    new_HistorialPagos = Pagos(Pagos)
    db.session.add(new_HistorialPagos)
    db.session.commit()
    return redirect("/Pagos")