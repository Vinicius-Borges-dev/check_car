from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locadora_veiculos.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    app.config['SECRET_KEY'] = 'ablublé'
    app.config['PERMANET_SESSION_LIFETIME'] = timedelta(days=1)
    
    from .routes.main import main_bp
    app.register_blueprint(main_bp)
    
    from .routes.user import user_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    
    from .routes.veiculo import veiculo_bp
    app.register_blueprint(veiculo_bp, url_prefix='/veiculo')
    
    from .routes.reserva import reserva_bp
    app.register_blueprint(reserva_bp, url_prefix='/reserva')

    return app