from unittest.mock import patch, MagicMock
from cache_service.lib.decorators import generate_cache_key, cache

def test_generate_cache_key():
    assert generate_cache_key("test", "cache:", [], {}) == "cache:test[]{}"

@patch("cache_service.lib.decorators.CacheService")
def test_cache_decorators(cache_service_mock):
    # Mock CacheService
    temp_dict = {}
    cache_service_mock_instance = cache_service_mock()
    cache_service_mock_instance.get = MagicMock(side_effect = lambda key: temp_dict.get(key))
    cache_service_mock_instance.set = MagicMock(side_effect = lambda key, value: temp_dict.__setitem__(key, value))

    @cache("test")
    def mock_fn():
        return 1
    
    key = generate_cache_key("test", "CACHE:", [], {})

    # Before calling the method, key should not be present in the cache
    assert temp_dict.get(key) is None

    mock_fn()

    assert cache_service_mock_instance.get.call_count == 1
    assert cache_service_mock_instance.set.call_count == 1
    assert temp_dict.get(key) == 1