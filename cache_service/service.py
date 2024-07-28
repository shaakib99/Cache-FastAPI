from cache_service.lib.cache_abc import CacheABC
from cache_service.redis_cache_service import RedisCacheService

class CacheService:
    def __init__(self, Service = RedisCacheService):
        self.service: CacheABC = Service.get_instance()
    
    def get(self, key: str) -> dict:
        pass

    def set(self, key: str, data: dict) -> None:
        pass

    def delete(self, key: str) -> None:
        pass
