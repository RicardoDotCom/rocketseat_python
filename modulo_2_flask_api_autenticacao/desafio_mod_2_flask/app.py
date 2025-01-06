from flask import Flask, request, jsonify
from models.refeicao import Refeicao
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/flask_crud_api_dieta"

db.init_app(app)

@app.route('/refeicao', methods=['POST'])
def incluir_refeicao():
    data = request.json
    refeicao = data.get("refeicao")
    descricao = data.get("descricao")
    data_refeicao = data.get("data_refeicao")
    esta_na_dieta = data.get("esta_na_dieta")

    if refeicao and descricao and data_refeicao and esta_na_dieta:    
        refeicao = Refeicao(refeicao=refeicao, descricao=descricao, data_refeicao=data_refeicao, esta_na_dieta=esta_na_dieta)
        db.session.add(refeicao)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com sucesso"})

    return jsonify({"message": "Dados inválidos"}), 400


if __name__ == '__main__':
    app.run(debug=True)