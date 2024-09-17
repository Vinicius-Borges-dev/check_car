from flask import Blueprint, render_template, request, redirect
from app.models import Veiculo

main_bp = Blueprint('main', __name__, static_folder='static')

@main_bp.route('/')
def index():
    return render_template('index.html')