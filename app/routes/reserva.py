from flask import Blueprint, render_template, request, redirect
from app.models import Reserva, Veiculo
from app import db

reserva_bp = Blueprint('reserva', __name__, static_folder='static', template_folder='templates/reservas')

@reserva_bp.route('/')
def index():
    reservas = Reserva.query.all()
    veiculo = Veiculo.query.find_by(id=reserva.id_veiculo)
    return render_template('index.html', reservas=reservas, veiculo=veiculo)