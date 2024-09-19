from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import Veiculo, Reserva
from app import db
from app.middlewares import AuthMiddleware
from werkzeug.utils import secure_filename

veiculo_bp = Blueprint('veiculo', __name__, static_folder='static')

@veiculo_bp.before_request
def loginAuth():
    if not AuthMiddleware.is_logged():
        return redirect(url_for('user.login'))

@veiculo_bp.route('/')
def index():
    veiculos = Veiculo.query.all()
    return render_template('veiculos/cards_veiculos.html', veiculos=veiculos)

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

        if AuthMiddleware.image_validation(imagem):
            imagemName = secure_filename(imagem.filename)
            imagem.save(f'app/static/carImages/{imagemName}')
        
            veiculo = Veiculo(marca=marca, modelo=modelo, placa=placa, categoria=categoria, ano=ano, precoDia=valor, imagem=imagemName, disponibilidade=status)
        
            db.session.add(veiculo)
            db.session.commit()
        
        return redirect('/veiculo')
    else:
        return render_template('veiculos/cadastro_veiculo.html')

@veiculo_bp.route('/deletar/<int:id>')
def deletar(id):
    if AuthMiddleware.get_employee_permission():
        veiculo = Veiculo.query.filter_by(id_veiculo=id).first()
        reservas = Reserva.query.filter_by(id_veiculo=veiculo.id_veiculo)
        db.session.delete(reservas)
        db.session.delete(veiculo)
        db.session.commit()
        return redirect('/veiculo')
    else:
        return redirect('/veiculo')

@veiculo_bp.route('/editar/<int:id>', methods=['GET','POST'])
def editar_veiculo(id):
    veiculo = Veiculo.query.filter_by(id_veiculo=id).first()
    if request.method == 'GET':
        return render_template('veiculos/editar_veiculo.html', veiculo=veiculo)
    else:
        imagem = request.files['imagem']
        if AuthMiddleware.image_validation(imagem):
            veiculo.marca = request.form['marca']
            veiculo.modelo = request.form['modelo']
            veiculo.placa = request.form['placa']
            veiculo.categoria = request.form['categoria']
            veiculo.ano = int(request.form['ano'])
            veiculo.precoDia = float(request.form['precoDia'].replace(',','.'))
            veiculo.status = request.form['status']
            imagemName = secure_filename(imagem.filename)
            imagem.save(f'app/static/carImages/{imagemName}')
            veiculo.imagem = imagem.filename
            db.session.commit()
        return redirect('/veiculo')