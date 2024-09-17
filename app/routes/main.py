from flask import Blueprint, render_template, request, redirect, session
from app.models import Veiculo
from app.middlewares import getAuthResponse

main_bp = Blueprint('main', __name__, static_folder='static')

@main_bp.route('/')
@getAuthResponse
def index():
    return render_template('index.html')
