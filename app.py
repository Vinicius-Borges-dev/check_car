from app import db, create_app
from app.models import DadosPessoais, Usuario, Veiculo, Manutencao, Reserva

app = create_app()

with app.app_context():
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)