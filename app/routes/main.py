from flask import Blueprint, render_template, request, redirect, session
from app.models import Veiculo
from app.middleware import AuthMiddleware

main_bp = Blueprint('main', __name__, static_folder='static')

@main_bp.before_request
def loginAuth():
    if not AuthMiddlware.is_logged():
        return redirect(url_for('user'))

@main_bp.route('/')
@getAuthResponse
def index():
    return render_template('index.html')
