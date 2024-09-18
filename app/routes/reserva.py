from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import Reserva, Veiculo, Usuario
from app import db
from app.middlewares import AuthMiddleware
from datetime import datetime, date

reserva_bp = Blueprint('reserva', __name__, static_folder='static', template_folder='templates/reservas')

@reserva_bp.before_request
def loginAuth():
    if not AuthMiddleware.is_logged():
        return redirect(url_for('user.login'))

@reserva_bp.route('/reservas')
def reservas():
    if not AuthMiddleware.get_employee_permission(): return redirect(url_for('main.index'))
    reservas = Reserva.query.all()
    veiculos = []
    usuarios = []
    for reserva in reservas:
        veiculos.append({
            'marca': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().marca,
            'modelo': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().modelo,
            'placa': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().placa,
        })
        usuarios.append({
            'nome': Usuario.query.filter_by(id_usuario=reserva.id_usuario).first().nome,
        })
    return render_template('reservas/reservas.html', reservas=reservas, veiculos=veiculos, usuarios=usuarios)

@reserva_bp.route('/minhas_reservas')
def minhas_reservas():
    reservas = Reserva.query.filter_by(id_usuario=session['id'])
    veiculos = []
    for reserva in reservas:
        veiculos.append({
            'marca': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().marca,
            'modelo': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().modelo,
            'placa': Veiculo.query.filter_by(id_veiculo=reserva.id_veiculo).first().placa,
        })
    return render_template('reservas/minhas_reservas.html', reservas=reservas , veiculos=veiculos)

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
    
    return redirect(url_for('reserva.minhas_reservas'))

@reserva_bp.route('/cancelar/<int:id>')
def cancelar(id):
    reserva = Reserva.query.filter_by(id_reserva=id).first()
    db.session.delete(reserva)
    db.session.commit()
    return redirect(url_for('reserva.minhas_reservas'))