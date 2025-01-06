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

@app.route('/refeicao', methods=['GET'])
def listar_refeicoes():
    refeicoes = Refeicao.query.all()

    if refeicoes:
        refeicoes_list = [refeicao.to_dict() for refeicao in refeicoes]
        return jsonify(refeicoes_list)
    
    return jsonify({"message": "Não há refeições cadastradas"}), 404

@app.route('/refeicao/<int:id_refeicao>', methods=['GET'])
def listar_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)

    if refeicao:
        return {           
        "refeicao": refeicao.refeicao,
        "descricao": refeicao.descricao,
        "data_refeicao": refeicao.data_refeicao,
        "esta_na_dieta": refeicao.esta_na_dieta
        }
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route('/refeicao/<int:id_refeicao>', methods=['PUT'])
def atualiza_refeicao(id_refeicao):
    data = request.json
    refeicao = Refeicao.query.get(id_refeicao)

    if refeicao:
        refeicao.refeicao = data.get("refeicao")
        refeicao.descricao = data.get("descricao")
        refeicao.data_refeicao = data.get("data_refeicao")
        refeicao.esta_na_dieta = data.get("esta_na_dieta")
        db.session.commit()

        return jsonify({"message": f"Refeição {id_refeicao} atualizada com sucesso"})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)