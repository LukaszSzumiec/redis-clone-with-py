import threading
import pytest

from src.tests.client import QuickClient, SeparatedClient
from src.main import TCPServer


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
