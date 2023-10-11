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

@routes_Descuentos.route("/Descuentos", methods=["GET"])
def Descuentos():
    returnall = Descuentos.query.all()
    resultado_Descuentos = Descuentos_Schema.dump(returnall)
    return jsonify(resultado_Descuentos)


# crud de usuarios
@routes_Descuentos.route("/eliminar_Descuentos/<IDDeduccion>", methods=["GET"])
def eliminar_Descuentos(IDDeduccion):
    IDDeduccion = Descuentos.query.get(IDDeduccion)
    db.session.delete(IDDeduccion)
    db.session.commit()
    return jsonify(DescuentosSchema.dump(IDDeduccion))


@routes_Descuentos.route("/actualizarDescuentos", methods=["POST"])
def actualizarDescuentos():
    IDDescuento = request.json["IDDescuento"]
    FechaAplicacionDescuento = request.json["IDDescuento"]
    TipoDescuento = request.json["TipoDescuento"]
    MontoDescuento = request.json["MontoDescuento"]
    DescripcionDescuento = request.json["DescripcionDescuento"]
    IDEmpleado = request.json["IDEmpleado"]
    Descuentos = Descuentos.query.get(IDDescuento)
    Descuentos.FechaAplicacionDescuento = FechaAplicacionDescuento
    Descuentos.TipoDescuento = TipoDescuento
    Descuentos.MontoDescuento = MontoDescuento
    Descuentos.DescripcionDescuento = DescripcionDescuento
    Descuentos.IDEmpleado = IDEmpleado
    db.session.commit()
    return redirect("/Descuentos")


@routes_Descuentos.route("/save_Descuentos", methods=["POST"])
def save_Descuentos():
    Descuentos = request.json[
        "IDDescuento, FechaAplicacionDescuento, TipoDescuento, MontoDescuento, DescripcionDescuento, IDEmpleado"
    ]
    print(Descuentos)
    new_Descuentos = Descuentos(Descuentos)
    db.session.add(new_Descuentos)
    db.session.commit()
    return redirect("/Descuentos")
