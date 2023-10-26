
import pytest
import fakeredis

@pytest.fixture(scope="session")
def fake_redis() -> fakeredis.FakeStrictRedis:
    """
    Create a fake Redis client.

    Returns: FakeRedis client
    """
    return fakeredis.FakeStrictRedis()