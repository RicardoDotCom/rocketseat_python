from src.models.sqlite.repository.interfaces.product_repository import ProductsRepositoryInterfaces
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterfaces
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductCreator:
    def __init__(self, redis_repo: RedisRepositoryInterfaces, product_repo: ProductsRepositoryInterfaces) -> None:
        self.__redis_repo = redis_repo
        self.__product_repo = product_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        name = body.get("name")
        price = body.get("price")
        quantity = body.get("quantity")

        self.__insert_in_sql(name, price, quantity)
        self.__insert_in_cache(name, price, quantity)

        return self.__format_response()

    def __insert_in_sql(self, name: str, price: float, quantity: int) -> None:
        self.__product_repo.insert_product(name, price, quantity)

    def __insert_in_cache(self, name: str, price: float, quantity: int) -> None:
        product_key = name
        value = f'{price}, {quantity}'
        self.__redis_repo.insert_ex(product_key, value, ex=60)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body= {
                "type": "PRODUCT",
                "count": 1,
                "message": "Produto cadastrado com sucesso!"
            }
        )