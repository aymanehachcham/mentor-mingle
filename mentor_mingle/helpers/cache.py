import os

import redis
from dotenv import load_dotenv

load_dotenv()


class Cache:
    """
    A class to interact with the Redis cache
    """

    def __init__(
        self,
        host: str = os.environ.get("REDIS_HOST"),
        port: str = os.environ.get("REDIS_PORT"),
        client=None,
    ):
        """
        Initialize the Cache class
        """
        # Set up the Redis client
        try:
            self.cache_client = client or redis.Redis(host=host, port=port, decode_responses=True)
            self.cache_client.ping()
        except Exception as e:
            raise ConnectionError("Could not connect to Redis Cache") from e

    def get_val(self, key: str) -> str:
        """
        Get a value from the cache

        Args:
            key (str): The key to get

        Returns:
            str: The value
        """
        return self.cache_client.get(key)

    def get_map(self, key: str) -> dict:
        """
        Get a map from the cache

        Args:
            key (str): The key to get

        Returns:
            dict: The map
        """
        return self.cache_client.hgetall(key)

    def set_map(self, key: str, map: dict) -> None:
        """
        Set a map in the cache

        Args:
            key (str): The key to set
            map (dict): The map to set

        Returns:
            None
        """
        self.cache_client.hset(key, mapping=map)

    def delete(self, key: str) -> None:
        """
        Delete a key from the cache

        Args:
            key (str): The key to delete

        Returns:
            None
        """
        self.cache_client.delete(key)
