from database import db

class Refeicao(db.Model):
    # id (int), username (text), password(text), role (text)
    id = db.Column(db.Integer, primary_key=True)
    refeicao = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data_refeicao = db.Column(db.DateTime(), nullable=False)
    esta_na_dieta = db.Column(db.Boolean(), nullable=False, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "refeicao": self.refeicao,
            "descricao": self.descricao,
            "data_refeicao": self.data_refeicao,
            "esta_na_dieta":self.esta_na_dieta
        }