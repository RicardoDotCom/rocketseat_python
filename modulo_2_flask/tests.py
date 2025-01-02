import pytest
import requests

# CRUD

# Iremos informar qual a url que será executado o teste
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

# Criamos uma função que irá simular a criação de uma tarefa, contendo todas as informações 
# necessárias para realizar a inclusão, depois iremos chamar na "request" o método "post" 
# informando o tipo e passando a váriavel toda vez que o request é acionado ele retorna 
# um objeto que iremos armazenar no "response" onde conseguimos validar se o teste obteve 
# sucesso neste exemplo se o "Status code" for igual a 200 o teste passou para isso colocamos
# ASSERT na validação que queremos confirmar
def test_create_task():
    new_task_data = {
        "title": "Nova Tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])