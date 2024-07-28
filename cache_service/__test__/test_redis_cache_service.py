from unittest.mock import MagicMock, patch

@patch("cache_service.redis_cache_service.RedisCacheService")
def test_redis_cache_service(redis_cache_service_mock):
    # assert redis_cache_service_mock.instance is None

    redis_cache_service_instance_mock = redis_cache_service_mock.get_instance()

    assert redis_cache_service_mock.instance is not None
    assert redis_cache_service_instance_mock == redis_cache_service_mock.get_instance()

    # Mock redis_cache_service
    temp_dict = {}
    redis_cache_service_instance_mock.get = MagicMock(side_effect = lambda key: temp_dict.get(key))
    redis_cache_service_instance_mock.set = MagicMock(side_effect = lambda key, value: temp_dict.__setitem__(key, value))
    redis_cache_service_instance_mock.delete = MagicMock(side_effect = lambda key: temp_dict.__delitem__(key))
    redis_cache_service_instance_mock.connect = MagicMock(return_value = None)
    redis_cache_service_instance_mock.disconnect = MagicMock(return_value = None)

    test_key = "test"
    test_value = {"test": 1}

    assert temp_dict.get(test_key) is None
    assert redis_cache_service_instance_mock.get(test_key) is None

    redis_cache_service_instance_mock.set(test_key, test_value)

    assert temp_dict.get(test_key) is not None
    assert temp_dict.get(test_key)["test"] == 1
    assert redis_cache_service_instance_mock.get(test_key)["test"] == 1

    redis_cache_service_instance_mock.delete(test_key)

    assert temp_dict.get(test_key) is None
