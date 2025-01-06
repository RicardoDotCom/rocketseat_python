from flask import Flask, request, jsonify
from models.refeicao import Refeicao
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"


db.init_app(app)