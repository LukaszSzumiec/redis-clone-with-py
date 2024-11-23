from threading import Thread


def test_first_message(tcp_server, client):
    response = client.send("Test")
    assert "Received" == response.decode()


def test_set_call(tcp_server, client):
    response = client.send("SET kappa 1").decode()
    assert "OK" == response

    response = client.send("GET kappa").decode()
    assert "1" == response


def test_delete_call(tcp_server, client):
    response = client.send("SET kappa 1").decode()
    assert "OK" == response

    response = client.send("DEL kappa").decode()
    assert "Deleted" == response

    response = client.send("GET kappa").decode()
    assert "NULL" == response
