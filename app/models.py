from . import db


class DadosPessoais(db.Model):
    __tablename__ = 'dados_pessoais'

    id_dados_pessoais = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    anoNascimento = db.Column(db.Integer, nullable=False)
    rg = db.Column(db.Integer, nullable=False)
    cpf = db.Column(db.Integer, nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.id_dados_pessoais

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return self.id_usuario

class Veiculo(db.Model):
    __tablename__ = 'veiculos'

    id_veiculo = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    precoDia = db.Column(db.Float, nullable=False)
    disponibilidade = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return self.id_veiculo

class Manutencao(db.Model):
    __tablename__ = 'manutencao'

    id_manutencao = db.Column(db.Integer, primary_key=True)
    id_veiculo = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    dataEntrada = db.Column(db.DateTime, nullable=False)
    dataSaida = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return self.id_manutencao

class Reserva(db.Model):
    __tablename__ = 'reserva'

    id_reserva = db.Column(db.Integer, primary_key=True)
    id_veiculo = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)
    dataInicio = db.Column(db.DateTime, nullable=False)
    dataFim = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return self.id_reserva