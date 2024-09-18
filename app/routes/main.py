from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import Veiculo
from app.middlewares import AuthMiddleware

main_bp = Blueprint('main', __name__, static_folder='static')

@main_bp.before_request
def loginAuth():
    if not AuthMiddleware.is_logged():
        return redirect(url_for('user.login'))

@main_bp.route('/')
def index():
    return render_template('veiculos/index.html')