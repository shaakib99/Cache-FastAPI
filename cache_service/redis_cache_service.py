from cache_service.lib.cache_abc import CacheABC

class RedisCacheService(CacheABC):
    def connect(self):
        pass

    def disconnect(self):
        pass
    
    @staticmethod
    def get_instance():
        pass

    def get(self, key: str) -> dict:
        pass

    def set(self,key: str, data: dict) -> None:
        pass

    def delete(self, key: str) -> None:
        pass
