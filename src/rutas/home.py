from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from common.Toke import *

routes_home = Blueprint("routes_home", __name__)



@routes_home.route('/indexpagar', methods=['GET'] )
def indexpagar():
    return render_template('/main/form_pago.html')

@routes_home.route('/indexhistorialpagos', methods=['GET'] )
def indexhistorialpagos():
    return render_template('/main/historial_pagos.html')

@routes_home.route('/indexcreditolibreinversion', methods=['GET'] )
def indexcreditolibreinversion():
    return render_template('/main/credito_libre_inversion.html')

@routes_home.route('/indexcreditolibreinversion2', methods=['GET'] )
def indexcreditolibreinversion2():
    return render_template('/main/creditolibreinversion2.html')

@routes_home.route('/indexcreditohipotecario', methods=['GET'] )
def indexcreditohipotecario():
    return render_template('/main/credito_hipotecario.html')

@routes_home.route('/indexcreditohipotecario2', methods=['GET'] )
def indexcreditohipotecario2():
    return render_template('/main/credito_hipotecario2.html')

@routes_home.route('/indexcreditoeducativo', methods=['GET'] )
def indexcreditoeducativo():
    return render_template('/main/credito_educativo.html')

@routes_home.route('/indexcreditoeducativo2', methods=['GET'] )
def indexcreditoeducativo2():
    return render_template('/main/credito_educativo2.html')
