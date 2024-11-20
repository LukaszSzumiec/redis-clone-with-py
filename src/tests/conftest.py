import threading
import pytest

from src.tests.client import Client
from src.main import TCPServer


@pytest.fixture()
def tcp_server():
    with TCPServer() as server:
        thread = threading.Thread(target=server.listen_for_requests)
        thread.daemon = True
        thread.start()
        yield server


@pytest.fixture()
def client():
    return Client()
