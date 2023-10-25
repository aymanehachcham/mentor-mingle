import os

from mentor_mingle.helpers.cache import Cache
import pytest
import fakeredis

class TestCache:

    @pytest.fixture
    def fake_redis(self):
        return fakeredis.FakeStrictRedis()


    def test_get(self, fake_redis):
        """
        Test the get method of the Cache class.
        """
        cache = Cache(client=fake_redis)
        cache.cache_client.set("test", "test")
        assert cache.get_val("test") == b"test"
        cache.cache_client.delete("test")

    def test_get_map(self, fake_redis):
        """
        Test the get_map method of the Cache class.
        """
        cache = Cache(client=fake_redis)
        cache.cache_client.hset("test_dict", mapping={
            "test_prompt": "Hello Assistant!",
            "test_response": "Hello User!"
        })
        assert cache.get_map("test_dict") == {
            b"test_prompt": b"Hello Assistant!",
            b"test_response": b"Hello User!"
        }
        cache.cache_client.delete("test_dict")

    def test_set_map(self, fake_redis):
        """
        Test the set_map method of the Cache class.
        """
        cache = Cache(client=fake_redis)
        cache.set_map("test", {"key": "val"})
        assert cache.cache_client.hgetall("test") == {b"key": b"val"}
        cache.cache_client.delete("test")