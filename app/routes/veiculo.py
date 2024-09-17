from flask import Blueprint, render_template, request, redirect
from app.models import Veiculo
from app import db

veiculo_bp = Blueprint('veiculo', __name__, static_folder='static')

@veiculo_bp.route('/')
def index():
    veiculos = Veiculo.query.all()
    return render_template('cards_veiculos.html', veiculos=veiculos)

@veiculo_bp.route('/adicionar_veiculo', methods=['GET','POST'])
def veiculos():
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
        return render_template('cadastro_veiculo.html')