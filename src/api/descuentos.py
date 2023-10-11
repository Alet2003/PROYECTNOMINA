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
from Model.descuentos import Descuentos, DescuentosSchema
routes_Descuentos = Blueprint("routes_Descuentos", __name__)

# usuario
Descuento_Schema = DescuentosSchema()
Descuentos_Schema = DescuentosSchema(many=True)

@routes_Descuentos.route("/Deducciones", methods=["GET"])
def Deducciones():
    returnall = Deducciones.query.all()
    resultado_Deducciones = Descuentos_Schema.dump(returnall)
    return jsonify(resultado_Deducciones)


# crud de usuarios
@routes_Descuentos.route("/eliminar_Deducciones/<IDDeduccion>", methods=["GET"])
def eliminar_Deducciones(IDDeduccion):
    IDDeduccion = Deducciones.query.get(IDDeduccion)
    db.session.delete(IDDeduccion)
    db.session.commit()
    return jsonify(DescuentosSchema.dump(IDDeduccion))


@routes_Descuentos.route("/actualizarDeducciones", methods=["POST"])
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


@routes_Descuentos.route("/save_Deducciones", methods=["POST"])
def save_Deducciones():
    Deducciones = request.json[
        "IDDeduccion, TipoDeduccion, MontoDeduccion, IDEmpleado"
    ]
    print(Deducciones)
    new_Deducciones = Deducciones(Deducciones)
    db.session.add(new_Deducciones)
    db.session.commit()
    return redirect("/Deducciones")
