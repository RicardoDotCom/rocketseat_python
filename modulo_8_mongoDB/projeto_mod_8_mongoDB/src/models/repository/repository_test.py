import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interaao com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "alguma": "coisa", "valor": 3 }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interaao com o banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{ "elem": "item1" }, { "elem": "item2" }, { "elem": "item3" }]
    orders_repository.insert_list_of_documents(my_doc)
