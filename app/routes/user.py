from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import Usuario , DadosPessoais
from app import db
from datetime import datetime, date

user_bp = Blueprint('user', __name__, static_folder='static')

@user_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('users/login.html')
    else:
        email = request.form['email']
        senha = request.form['password']
        dadosPessoais = DadosPessoais.query.filter_by(email=email).first()
        usuario = Usuario.query.filter_by(id_usuario=dadosPessoais.id_usuario).first()
        if email == dadosPessoais.email and senha == usuario.senha:
            session['id'] = usuario.id_usuario
            session['tipo'] = usuario.tipo
            session.permanent = True
            return redirect(url_for('main.index'))
        else:
            return redirect(url_for('user.login'))


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
        db.session.add(novo_usuario)
        db.session.commit()

        dados_pessoais = DadosPessoais(
            endereco = request.form['endereco'],
            email = request.form['email'],
            dataNascimento = datetime.strptime(request.form['dataNascimento'], '%Y-%m-%d'),
            rg = request.form['rg'],
            cpf = request.form['cpf'],
            telefone = request.form['telefone'],
            id_usuario = Usuario.query.filter_by(nome=request.form['username']).first().id_usuario
        )
        db.session.add(dados_pessoais)
        db.session.commit()

        return redirect(url_for('user.login'))
    
@user_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))