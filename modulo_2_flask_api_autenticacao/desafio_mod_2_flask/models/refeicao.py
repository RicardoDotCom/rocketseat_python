from database import db

class User(db.Model):
    # id (int), username (text), password(text), role (text)
    id = db.Column(db.Integer, primary_key=True)
    refeicao = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data_refeicao = db.Column(db.DateTime(), nullable=False)
    dieta = db.Column(db.Boolean(), nullable=False, default=False)