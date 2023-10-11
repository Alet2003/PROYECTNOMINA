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
from Model.empleados import Empleados, EmpleadosSchema
now = datetime.now()
routes_empleados = Blueprint("routes_empleados", __name__)

# usuario
Empleado_Schema = EmpleadosSchema()
Empleados_Schema = EmpleadosSchema(many=True)

@routes_empleados.route("/Empleados", methods=["GET"])
def Empleados():
    returnall = Empleados.query.all()
    resultado_empleados = Empleados_Schema.dump(returnall)
    return jsonify(resultado_empleados)


# crud de usuarios
@routes_empleados.route("/eliminar_Users/<IDEmpleado>", methods=["GET"])
def eliminar_users(IDEmpleado):
    IDEmpleado = Empleados.query.get(IDEmpleado)
    db.session.delete(IDEmpleado)
    db.session.commit()
    return jsonify(EmpleadosSchema.dump(IDEmpleado))


@routes_empleados.route("/actualizarUsers", methods=["POST"])
def actualizar_users():
    IDEmpleado = request.json["IDEmpleado"]
    nombre = request.json["Nombre"]
    Apellido = request.json["Apellido"]
    fecha_nacimiento = request.json["FechaNacimiento"]
    direccion = request.json["Direccion"]
    telefono = request.json["NumeroTelefono"]
    correo = request.json["CorreoElectronico"]
    Departamento = request.json["Departamento"]
    FechaContratacion = request.json["FechaContratacion"]
    SalarioBase = request.json["SalarioBase"]
    Empleados = Empleados.query.get(IDEmpleado)
    Empleados.nombre = nombre
    Empleados.Apellido = Apellido
    Empleados.fecha_nacimiento = fecha_nacimiento
    Empleados.direccion = direccion
    Empleados.telefono = telefono
    Empleados.correo = correo
    Empleados.Departamento = Departamento
    Empleados.FechaContratacion = FechaContratacion
    Empleados.SalarioBase = SalarioBase
    db.session.commit()
    return redirect("/Empleados")


@routes_empleados.route("/save_Users", methods=["POST"])
def guardar_Users():
    Empleados = request.json[
        "IDEmpleado, Nombre, Apellido, FechaNacimiento, Direccion, NumeroTelefono, CorreoElectronico, Departamento, FechaContratacion, SalarioBase"
    ]
    print(Empleados)
    new_empleado = Empleados(Empleados)
    db.session.add(new_empleado)
    db.session.commit()
    return redirect("/Usuarios")


# @routes_empleados.route("/save_registro", methods=["POST"])
# def registrar():
#     id = request.form["id"]
#     nombre = request.form["nombre"]
#     fecha_nacimiento= request.form["fecha_nacimiento"] 
#     correo = request.form["correo"]
#     password = request.form["password"]
#     telefono=request.form["telefono"]
#     direccion= request.form["direccion"]
#     fecha_registro = now.date()
#     id_roles = request.form["id_roles"]
#     new_registro = Empleados(id, nombre, fecha_nacimiento, correo, password, telefono, direccion, fecha_registro, "", id_roles)
#     db.session.add(new_registro)
#     db.session.commit()
#     return ""


# @app.route("/login", methods=["POST"])
# def login():
#         correo = request.json["correo"]
#         password = request.json["password"]
#         resultado = (
#         db.session.query(Empleados, RolesUsuarios)
#         .filter(
#             Empleados.correo == correo,
#             Empleados.password == password,
#             Empleados.id_roles == RolesUsuarios.id
#         ).first()
#         )
#         user_token = correo
#         pass_token = password
#         # Llamada a la función generar_token para obtener el token y los datos
#         tokeng = generar_token(user_token, pass_token)
#         token = tokeng['token']
#         vf = verificar_token(token)
#         if vf['error'] == False:
#             # Busca el usuario en la base de datos
#             if not resultado:
#                 return "a" #jsonify({"": ""+})

#             # Si el inicio de sesión es exitoso, redirige al usuario a la vista correspondiente en función de su id_roles
#         if resultado.RolesUsuarios.roles == "Secretaria":
#                 session['correo_usuario'] = correo
#                 session['token'] = token
#                 return jsonify({"rol": "Secretaria"})

#             # return redirect("/fronted/indexagendarcitas")
#         elif resultado.RolesUsuarios.roles == "Odontologo":
#                 session['token'] = token
#                 session['correo_usuario'] = correo
#                 return jsonify({"rol": "Odontologo"})

#                 # return redirect("/main/homeodontologo.html")
#         elif resultado.RolesUsuarios.roles == "Paciente":
#                 session['token'] = token
#                 session['correo_usuario'] = correo
#                 return jsonify({"rol": "Paciente"})

#                 # return redirect("/main/homepaciente.html")
#         else:
#              return vf

        

# @routes_empleados.route('/misdatos', methods=['GET'])
# def misdatos():
#     correo= session.get('correo_usuario')
#     datos= {}
#     resultado = db.session.query(Users).select_from(Users).filter(Users.correo == correo).all()
#     users = []
#     i = 0
#     for usuarios in resultado:
#         i += 1
#         datos[i] = {
#         'id':usuarios.id,
# 		'nombre':usuarios.nombre,
# 		'fecha_nacimiento':usuarios.fecha_nacimiento,
# 		'correo':usuarios.correo,
# 		'password':usuarios.password,
# 		'telefono':usuarios.telefono,
# 		'direccion': usuarios.direccion,              
# 		'fecha_registro': usuarios.fecha_registro,
#         'rol': usuarios.id_roles                      
#         }
#     users.append(datos)
#     return jsonify(datos)

# @app.route('/estadisticas', methods=['POST'])
# def estadisticas():
#     datos= {}
#     correo= session.get('correo_usuario')
#     fecha_inicio = datetime.strptime(request.json['fecha_inicio'], '%Y-%m-%d').date()
#     fecha_fin = datetime.strptime(request.json['fecha_fin'], '%Y-%m-%d').date()
#     print(correo)
#     stats = []

#     first_day = fecha_inicio - timedelta(days=fecha_inicio.weekday())
#     i=0
#     while first_day <= fecha_fin:
#         i += 1
#         last_day = first_day + timedelta(days=6)

#         num_pacientes = db.session.query(func.count(Users.id)).join(citas, citas.id_odontologo == Users.id).\
#             filter(citas.fecha.between(first_day, last_day), Users.correo==correo).scalar()

#         porcentaje = round((num_pacientes / 10) * 100)
#         print(porcentaje)
#         datos[i] ={
#             'semana': f'{first_day.strftime("%d/%m/%Y")} - {last_day.strftime("%d/%m/%Y")}',
#             'pacientes_atendidos': num_pacientes,
#             'porcentaje': porcentaje
#         }
#         stats.append(datos)

#         first_day = last_day + timedelta(days=1)

#     return jsonify(datos)

# @app.route('/estadisticasmensuales', methods=['POST'])
# def estadisticames():
#     datos= {}
#     correo= session.get('correo_usuario')
#     fecha_inicio = datetime.strptime(request.json['fecha_inicio'], '%Y-%m-%d').date()
#     fecha_fin = datetime.strptime(request.json['fecha_fin'], '%Y-%m-%d').date()
#     print(correo)
#     stats = []

#     numDmes=(fecha_fin - fecha_inicio).days+1

#     first_day = fecha_inicio.replace(day=1)
#     last_day = fecha_inicio.replace(day=28) + timedelta(days=4)
#     ultiDmes= last_day -  timedelta(days=last_day.day)

#     num_pacientes = db.session.query(func.count(Users.id)).join(citas, citas.id_odontologo == Users.id).\
#             filter(citas.fecha.between(first_day, last_day), Users.correo==correo).scalar()

#     porcentaje = round((num_pacientes / 40) * 100)

    

#     datos={
#             'mes': first_day.strftime('%B  %Y'),
#             'pacientes_atendidos': num_pacientes,
#             'porcentaje': porcentaje
#         }-
    
#     return jsonify(datos)

# @routes_empleados.route('/actualizardatos', methods=['POST'] )
# def actualizardatos():
#     correo= session.get('correo_usuario')
#     resultado = (db.session.query(Users).filter(Users.correo==correo).first())
#     nombre = request.json['nombre']
#     correoo =request.json['correo']
#     telefono= request.json['telefono']
#     direccion= request.json['direccion']
#     password= request.json['password']
#     fecha_actualizacion = now.date()
#     print(nombre, correo, telefono, correoo, password)
    
#     if resultado is not None:
#         id=resultado.id
#         fecha_nacimiento=resultado.fecha_nacimiento
#         fecha_registro =resultado.fecha_registro
#         users = Users.query.filter_by(correo=correo).first()
#         users.id = id
#         users.nombre = nombre
#         users.fecha_nacimiento = fecha_nacimiento
#         users.correo = correoo
#         users.password= password
#         users.telefono = telefono
#         users.direccion= direccion
#         users.fecha_registro=fecha_registro
#         users.fecha_actualizacion= fecha_actualizacion
#         db.session.commit()
#         return "Datos actualizados correctamente"
#     else:
#         return "Error: No se actualizaron los datos"

# @routes_empleados.route('/cerrar_sesion', methods=['POST'])
# def cerrar_sesion():
#     print("llego")
#     datos = request.json
#     dato = datos['sesion']
#     if dato == "sesion_cerrada":
#         if 'token' in session:
#             print("elimino")
#             del session['token']
#             return ""
#         else:
#             return ""

# @routes_empleados.route('/movimiento', methods=['POST'])
# def movimiento():
#     datos = request.json
#     dato = datos['movi']
#     if dato == "se movio":
#             token = session.get('token')
#             vf = verificar_token(token)
#             if vf['error'] == False:
#                 print("token valido")
#                 return ""
#             else:
#                 print("token vencido")
#                 return "algo"

    
# @routes_empleados.route('/mispac', methods=['GET'])
# def mispac():
#     datos= {}
#     resultado = db.session.query(Users).filter(Users.id_roles == 3).all()
#     users = []
#     i = 0
#     for usuarios in resultado:
#         i += 1
#         datos[i] = {
#         'id':usuarios.id,
# 		'nombre':usuarios.nombre,
# 		'fecha_nacimiento':usuarios.fecha_nacimiento,
# 		'correo':usuarios.correo,
# 		'telefono':usuarios.telefono
#         }
#     users.append(datos)
#     return jsonify(datos)

# @routes_empleados.route('/misodon', methods=['GET'])
# def misodon():
#     datos= {}
#     resultado = db.session.query(Users).filter(Users.id_roles == 2).all()
#     users = []
#     i = 0
#     for usuarios in resultado:
#         i += 1
#         datos[i] = {
#         'id':usuarios.id,
# 		'nombre':usuarios.nombre,
# 		'fecha_nacimiento':usuarios.fecha_nacimiento,
# 		'correo':usuarios.correo,
# 		'telefono':usuarios.telefono
#         }
#     users.append(datos)
#     return jsonify(datos)
