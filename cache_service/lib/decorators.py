from cache_service.service import CacheService
import json
from functools import wraps

def cache(key: str):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            cache_service = CacheService()

            new_key = generate_cache_key(key, "CACHE:", args, kwargs)
            data = cache_service.get(new_key) 
            if data is not None: 
                return {"message": "Cache Hit"}
            
            result = func(*args, **kwargs)
            cache_service.set(new_key, result)
            return {"message": "Cache Miss"}
        return inner
    return wrapper

def generate_cache_key(old_key, prefix, args, kwargs) -> str:
    return f"{prefix}{old_key}{json.dumps(args)}{json.dumps(kwargs)}"