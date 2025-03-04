from src.models.sqlite.repository.interfaces.product_repository import ProductsRepositoryInterfaces
from src.models.redis.repository.interfaces.redis_repository import RedisRepositoryInterfaces

class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterfaces, product_repo: ProductsRepositoryInterfaces) -> None:
        self.__redis_repo = redis_repo
        self.__product_repo = product_repo
