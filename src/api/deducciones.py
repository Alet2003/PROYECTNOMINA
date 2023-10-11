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
from Model.deducciones import Deducciones, DeduccionesSchema
routes_Deducciones = Blueprint("routes_Deducciones", __name__)

# usuario
Deduccion_Schema = DeduccionesSchema()
Deducciones_Schema = DeduccionesSchema(many=True)

@routes_Deducciones.route("/Deducciones", methods=["GET"])
def Deducciones():
    returnall = Deducciones.query.all()
    resultado_Deducciones = Deducciones_Schema.dump(returnall)
    return jsonify(resultado_Deducciones)


# crud de usuarios
@routes_Deducciones.route("/eliminar_Deducciones/<IDDeduccion>", methods=["GET"])
def eliminar_Deducciones(IDDeduccion):
    IDDeduccion = Deducciones.query.get(IDDeduccion)
    db.session.delete(IDDeduccion)
    db.session.commit()
    return jsonify(DeduccionesSchema.dump(IDDeduccion))


@routes_Deducciones.route("/actualizarDeducciones", methods=["POST"])
def actualizarDeducciones():
    IDDeduccion = request.json["IDDeduccion"]
    TipoDeduccion = request.json["TipoDeduccion"]
    MontoDeduccion = request.json["MontoDeduccion"]
    IDEmpleado = request.json["IDEmpleado"]
    Deducciones = Deducciones.query.get(IDDeduccion)
    Deducciones.TipoDeduccion = TipoDeduccion
    Deducciones.MontoDeduccion = MontoDeduccion
    Deducciones.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/Deducciones")


@routes_Deducciones.route("/save_Deducciones", methods=["POST"])
def save_Deducciones():
    Deducciones = request.json[
        "IDDeduccion, TipoDeduccion, MontoDeduccion, IDEmpleado"
    ]
    print(Deducciones)
    new_Deducciones = Deducciones(Deducciones)
    db.session.add(new_Deducciones)
    db.session.commit()
    return redirect("/Deducciones")
