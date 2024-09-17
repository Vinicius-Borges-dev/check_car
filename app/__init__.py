from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locadora_veiculos.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    from .routes.veiculo import veiculo_bp
    app.register_blueprint(veiculo_bp, url_prefix='/veiculo')
    
    from .routes.reserva import reserva_bp
    app.register_blueprint(reserva_bp, url_prefix='/reserva')

    return app