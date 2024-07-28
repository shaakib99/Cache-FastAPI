from unittest.mock import MagicMock
from cache_service.service import CacheService

def test_cache_service():
    cache_service = CacheService()



    # Mock cache_service
    temp_dict = {}
    cache_service.service.get = MagicMock(side_effect = lambda key: temp_dict.get(key))
    cache_service.service.set = MagicMock(side_effect = lambda key, value: temp_dict.__setitem__(key, value))
    cache_service.service.delete = MagicMock(side_effect = lambda key: temp_dict.__delitem__(key))
    cache_service.service.connect = MagicMock(return_value = None)
    cache_service.service.disconnect = MagicMock(return_value = None)

    test_key = "test"
    test_value = {"test": 1}

    assert temp_dict.get(test_key) is None

    cache_service.set(test_key, test_value)

    assert temp_dict.get(test_key) is not None
    assert temp_dict.get(test_key)["test"] == 1
    assert cache_service.get(test_key)["test"] == 1


    cache_service.delete(test_key)

    assert temp_dict.get(test_key) is None
