from flask import Blueprint, render_template, request, redirect
from app.models import Usuario
from app import db

user_bp = Blueprint('user', __name__, static_folder='static')

@user_bp.route('/')
def index():
    return render_template('conta/login.html')

@user_bp.route('/login', methods=['POST'])
def login():
    pass


@user_bp.route('/cadastro', methods=['POST'])
def cadastro():
    newUsuario = Usuario(
        nome = request.form['nome']
    )