from src.models.sqlite.repository.interfaces.product_repository import ProductsRepositoryInterfaces
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterfaces
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterfaces, product_repo: ProductsRepositoryInterfaces) -> None:
        self.__redis_repo = redis_repo
        self.__product_repo = product_repo

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse: pass 

