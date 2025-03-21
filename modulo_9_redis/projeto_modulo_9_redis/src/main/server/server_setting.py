from flask import Flask

from src.models.redis.settings.connection import RedisConnectionHandle
from src.models.sqlite.settings.connection import SqliteConnectionHandle


redis_connection_handle = RedisConnectionHandle()
sqlite_connection_handle = SqliteConnectionHandle()

redis_connection_handle.connect()
sqlite_connection_handle.connect()

app = Flask(__name__)

from src.main.routes.products_routes import product_routes_bp

app.register_blueprint(product_routes_bp)