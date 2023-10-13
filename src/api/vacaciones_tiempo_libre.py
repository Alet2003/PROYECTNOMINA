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
from Model.vacaciones_tiempo_libre import VacacionesTiempoLibre, VacacionesTiempoLibreSchema
now = datetime.now()
routes_VacacionesTiempoLibre = Blueprint("routes_VacacionesTiempoLibre", __name__)

# usuario
VacacionTiempoLibre_Schema = VacacionesTiempoLibreSchema()
VacacionesTiempoLibre_Schema = VacacionesTiempoLibreSchema(many=True)

@routes_VacacionesTiempoLibre.route("/VacacionesTiempoLibre", methods=["GET"])
def VacacionesTiempoLibre():
    returnall = VacacionesTiempoLibre.query.all()
    resultado_vtl = VacacionesTiempoLibre_Schema.dump(returnall)
    return jsonify(resultado_vtl)


# crud de usuarios
@routes_VacacionesTiempoLibre.route("/eliminar_VacacionesTiempoLibre/<IDSolicitud>", methods=["GET"])
def eliminar_VacacionesTiempoLibre(IDSolicitud):
    IDSolicitud = VacacionesTiempoLibre.query.get(IDSolicitud)
    db.session.delete(IDSolicitud)
    db.session.commit()
    return jsonify(VacacionesTiempoLibreSchema.dump(IDSolicitud))


@routes_VacacionesTiempoLibre.route("/actualizarVacacionesTiempoLibre", methods=["POST"])
def actualizarVacacionesTiempoLibre():
    IDSolicitud = request.json["IDSolicitud"]
    TipoSolicitud = request.json["TipoSolicitud"]
    FechaSolicitud = request.json["FechaSolicitud"]
    FechaInicio = request.json["FechaInicio"]
    FechaTermino = request.json["FechaTermino"]
    EstadoSolicitud = request.json["EstadoSolicitud"]
    IDEmpleado = request.json["IDEmpleado"]
    Creditos = Creditos.query.get(IDSolicitud)
    Creditos.TipoSolicitud = TipoSolicitud
    Creditos.FechaSolicitud = FechaSolicitud
    Creditos.FechaInicio = FechaInicio
    Creditos.FechaTermino = FechaTermino
    Creditos.EstadoSolicitud = EstadoSolicitud
    Creditos.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/actualizarVacacionesTiempoLibre")


@routes_VacacionesTiempoLibre.route("/save_VacacionesTiempoLibre", methods=["POST"])
def save_VacacionesTiempoLibre():
    VacacionesTiempoLibre = request.json[
        "IDSolicitud, TipoSolicitud, FechaSolicitud, FechaInicio, FechaTermino, EstadoSolicitud, IDEmpleado"
    ]
    print(VacacionesTiempoLibre)
    new_vtl = VacacionesTiempoLibre(VacacionesTiempoLibre)
    db.session.add(new_vtl)
    db.session.commit()
    return redirect("/VacacionesTiempoLibre")
