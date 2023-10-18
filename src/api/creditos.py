from flask import Flask, Blueprint,redirect,request,jsonify,json,session,render_template
from common.Toke import *
from config.db import db, app, ma
from sqlalchemy import func, extract
from datetime import datetime

from Model.creditos import Creditos, CreditosSchema

now = datetime.now()
routes_Creditos = Blueprint("routes_Creditos", __name__)

# usuario
CreditoSchema = CreditosSchema()
Creditos_Schema = CreditosSchema(many=True)

@routes_Creditos.route("/Creditos", methods=["GET"])
def Creditos():
    returnall = Creditos.query.all()
    resultado_creditos = Creditos_Schema.dump(returnall)
    return jsonify(resultado_creditos)


# crud de usuarios
@routes_Creditos.route("/eliminar_credito/<IDCredito>", methods=["GET"])
def eliminar_credito(IDCredito):
    IDCredito = Creditos.query.get(IDCredito)
    db.session.delete(IDCredito)
    db.session.commit()
    return jsonify(CreditosSchema.dump(IDCredito))


@routes_Creditos.route("/actualizarcreditos", methods=["POST"])
def actualizarcreditos():
    IDCredito = request.json["IDCredito"]
    FechaOtorgamiento = request.json["FechaOtorgamiento"]
    MontoCredito = request.json["MontoCredito"]
    TasaInteres = request.json["TasaInteres"]
    PlazoCredito = request.json["PlazoCredito"]
    CuotasMensuales = request.json["CuotasMensuales"]
    EstadoCredito = request.json["EstadoCredito"]
    IDEmpleado = request.json["IDEmpleado"]
    Creditos = Creditos.query.get(IDCredito)
    Creditos.FechaOtorgamiento = FechaOtorgamiento
    Creditos.MontoCredito = MontoCredito
    Creditos.TasaInteres = TasaInteres
    Creditos.PlazoCredito = PlazoCredito
    Creditos.CuotasMensuales = CuotasMensuales
    Creditos.EstadoCredito = EstadoCredito
    Creditos.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/Creditos")


@routes_Creditos.route("/save_creditos", methods=["POST"])
def save_creditos():
    Creditos = request.json[
        "IDCredito, FechaOtorgamiento, MontoCredito, TasaInteres, PlazoCredito, CuotasMensuales, EstadoCredito,IDEmpleado"
    ]
    print(Creditos)
    new_credito = Creditos(Creditos)
    db.session.add(new_credito)
    db.session.commit()
    return redirect("/Creditos")
