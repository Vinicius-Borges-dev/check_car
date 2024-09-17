from flask import Blueprint, render_template, request, redirect
from app.models import Reserva, Veiculo
from app import db

reserva_bp = Blueprint('reserva', __name__, static_folder='static', template_folder='templates/reservas')

@reserva_bp.route('/')
def index():
    reservas = Reserva.query.all()
    return render_template('reservas/index.html', reservas=reservas)

@reserva_bp.route('/form/<int:id>')
def form(id):
    return render_template('reservas/cadastrar_reserva.html', veiculo=Veiculo.query.get(id))

@reserva_bp.route('/cadastro/<int:id>', methods=['POST'])
def cadastro(id):
    novaReserva = Reserva(
        id_veiculo=id,
        id_usuario=session['id'],
        dataInicio=request.form['dataInicio'],
        dataFim=request.form['dataFim'],
        status=1
    )
    
    db.session.add(novaReserva)
    db.session.commit()
    
    return redirect('/reserva')