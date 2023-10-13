from datetime import datetime
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
from Model.resgistro_horas_trabajadas import RegistroHorasTrabajadas, RegistroHorasTrabajadasSchema
now = datetime.now()
routes_RegistroHorasTrabajadas = Blueprint("routes_RegistroHorasTrabajadas", __name__)

# usuario
RegistroHorasTrabajada_Schema = RegistroHorasTrabajadasSchema()
RegistroHorasTrabajadas_Schema = RegistroHorasTrabajadasSchema(many=True)

@routes_RegistroHorasTrabajadas.route("/RegistroHorasTrabajadas", methods=["GET"])
def RegistroHorasTrabajadas():
    returnall = RegistroHorasTrabajadas.query.all()
    resultado_rht = RegistroHorasTrabajadas_Schema.dump(returnall)
    return jsonify(resultado_rht)


# crud de usuarios
@routes_RegistroHorasTrabajadas.route("/eliminar_RegistroHorasTrabajadas/<IDRegistro>", methods=["GET"])
def eliminar_RegistroHorasTrabajadas(IDRegistro):
    IDRegistro = RegistroHorasTrabajadas.query.get(IDRegistro)
    db.session.delete(IDRegistro)
    db.session.commit()
    return jsonify(RegistroHorasTrabajadasSchema.dump(IDRegistro))


@routes_RegistroHorasTrabajadas.route("/actualizarRegistroHorasTrabajadas", methods=["POST"])
def actualizarRegistroHorasTrabajadas():
    IDRegistro = request.json["IDRegistro"]
    FechaRegistro = request.json["FechaRegistro"]
    HoraEntrada = request.json["HoraEntrada"]
    HoraSalida = request.json["HoraSalida"]
    TotalHorasTrabajadas = request.json["TotalHorasTrabajadas"]
    IDEmpleado = request.json["IDEmpleado"]
    RegistroHorasTrabajadas = RegistroHorasTrabajadas.query.get(IDRegistro)
    RegistroHorasTrabajadas.FechaRegistro = FechaRegistro
    RegistroHorasTrabajadas.HoraEntrada = HoraEntrada
    RegistroHorasTrabajadas.HoraSalida = HoraSalida
    RegistroHorasTrabajadas.TotalHorasTrabajadas = TotalHorasTrabajadas
    RegistroHorasTrabajadas.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/RegistroHorasTrabajadas")


@routes_RegistroHorasTrabajadas.route("/save_RegistroHorasTrabajadas", methods=["POST"])
def save_RegistroHorasTrabajadas():
    RegistroHorasTrabajadas = request.json[
        "IDRegistro, FechaRegistro, HoraEntrada, HoraSalida, TotalHorasTrabajadas, IDEmpleado"
    ]
    print(RegistroHorasTrabajadas)
    new_rht = RegistroHorasTrabajadas(RegistroHorasTrabajadas)
    db.session.add(new_rht)
    db.session.commit()
    return redirect("/RegistroHorasTrabajadas")
