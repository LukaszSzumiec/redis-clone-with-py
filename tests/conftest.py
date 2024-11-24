import threading
import pytest

from client import QuickClient, SeparatedClient
from redis.app import TCPServer


@pytest.fixture()
def tcp_server():
    with TCPServer() as server:
        thread = threading.Thread(target=server.listen_for_requests)
        thread.daemon = True
        thread.start()
        yield server


@pytest.fixture()
def quick_client():
    return QuickClient()


@pytest.fixture()
def separated_client():
    return SeparatedClient
