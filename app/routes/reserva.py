from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import Reserva, Veiculo
from app import db
from app.middlewares import AuthMiddleware
from datetime import datetime, date

reserva_bp = Blueprint('reserva', __name__, static_folder='static', template_folder='templates/reservas')

@reserva_bp.before_request
def loginAuth():
    if not AuthMiddleware.is_logged():
        return redirect(url_for('user.login'))

@reserva_bp.route('/')
def index():
    reservas = Reserva.query.filter_by(id_usuario=session['id'])
    veiculos = []
    for reserva in reservas:
        veiculos.append({
            'marca': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().marca,
            'modelo': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().modelo,
            'placa': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().placa,
        })
    return render_template('reservas/index.html', reservas=reservas , veiculos=veiculos)

@reserva_bp.route('/form/<int:id>')
def form(id):
    return render_template('reservas/cadastrar_reserva.html', veiculo=Veiculo.query.get(id))

@reserva_bp.route('/cadastro/<int:id>', methods=['POST'])
def cadastro(id):
    novaReserva = Reserva(
        id_veiculo=id,
        id_usuario=session['id'],
        dataInicio=datetime.strptime(request.form['dataInicial'], '%Y-%m-%d').date(),
        dataFim=datetime.strptime(request.form['dataFinal'], '%Y-%m-%d').date(),
        status=1
    )
    
    db.session.add(novaReserva)
    db.session.commit()
    
    return redirect('/reserva')