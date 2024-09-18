from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Usuario , DadosPessoais
from app import db

user_bp = Blueprint('user', __name__, static_folder='static')

@user_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('users/login.html')


@user_bp.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('users/cadastro.html')
    else:
        novo_usuario = Usuario(
            nome = request.form['username'],
            senha = request.form['password'],
            tipo = 'cliente',
            status = 1
        )
        
        dados_pessoais = DadosPessoais(
            endereco = request.form['endereco'],
            email = request.form['email'],
            dataNascimento = request.form['dataNascimento'],
            rg = request.form['rg'],
            cpf = request.form['cpf'],
            telefone = request.form['telefone'],
            id_usuario = novo_usuario.id_usuario
        )
        
        db.session.add(novo_usuario)
        db.session.add(dados_pessoais)
        db.session.commit()

        return redirect(url_for('user.login'))