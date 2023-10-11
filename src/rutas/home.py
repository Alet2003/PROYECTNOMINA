from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from common.Toke import *

routes_home = Blueprint("routes_home", __name__)


@routes_home.route('/indexmisodon', methods=['GET'] )
def indexmisodon():
    return render_template('/main/Dentistas.html')

@routes_home.route('/indexmispac', methods=['GET'] )
def indexmispac():
    return render_template('/main/pacienteO.html')
