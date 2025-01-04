from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"

# Trecho de código sugerido pelo Chatgpt onde na variável BASE_DIR é informado o caminho absoluto
# e na variável INSTANCE_DIR receberia o caminho completo da base de dados 

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(INSTANCE_DIR, 'database.db')}"


# Trecho do código sugerido pelo professor na aula porém causa um problema onde database.db é chamado na raiz do projeto 
# e não na pasta dele causando assim um erro ao fazer a chamada pelo postman, nas pesquisas que fiz houve uma sugestão de 
# criar a base de dados pelo próprio código e não utilizando o FLASK SHELL, também será estudado futuramente

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

print(f"Database path: {os.path.join(BASE_DIR, 'database.db')}")
print(f"Database path: {os.path.join(INSTANCE_DIR, 'database.db')}")


login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

# view login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
    
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Atenticação realizada com sucesso"})
    
    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso!"})

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuário cadastrado com sucesso"})

    return jsonify({"message": "Dados inválidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)