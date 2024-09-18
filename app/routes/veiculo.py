from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import Veiculo
from app import db
from app.middlewares import AuthMiddleware

veiculo_bp = Blueprint('veiculo', __name__, static_folder='static')

@veiculo_bp.before_request
def loginAuth():
    if not AuthMiddleware.is_logged():
        return redirect(url_for('user.login'))

@veiculo_bp.route('/')
def index():
    veiculos = Veiculo.query.all()
    return render_template('veiculos/cards_veiculos.html', veiculos=veiculos , nivel=session['tipo'])

@veiculo_bp.route('/adicionar_veiculo', methods=['GET','POST'])
def adicionar_veiculo():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        placa = request.form['placa']
        categoria = request.form['categoria']
        ano = int(request.form['ano'])
        valor = float(request.form['valor'].replace(',','.'))
        status = request.form['status']
        imagem = request.files['imagem']
        
        imagem.save(f'app/static/carImages/{imagem.filename}')
        
        veiculo = Veiculo(marca=marca, modelo=modelo, placa=placa, categoria=categoria, ano=ano, precoDia=valor, imagem=imagem.filename, disponibilidade=status)
        
        db.session.add(veiculo)
        db.session.commit()
        
        return redirect('/veiculo')
    else:
        return render_template('veiculos/cadastro_veiculo.html')

@veiculo_bp.route('/deletar/<int:id>')
def deletar(id):
    if AuthMiddleware.get_employee_permission():
        veiculo = Veiculo.query.filter_by(id_veiculo=id).first()
        db.session.delete(veiculo)
        db.session.commit()
        return redirect('/veiculo')
    else:
        return redirect('/veiculo')