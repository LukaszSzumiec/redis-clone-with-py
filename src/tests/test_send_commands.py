def test_first_message(tcp_server, client):
    response = client.send("Test")
    assert response.decode() == ""


def test_set_call(tcp_server, client):
    response = client.send("SET kappa 1").decode()
    assert response == "OK"

    response = client.send("GET kappa").decode()
    assert response == "1"


def test_delete_call(tcp_server, client):
    response = client.send("SET kappa 1").decode()
    assert response == "OK"

    response = client.send("DEL kappa").decode()
    assert response == "Deleted"

    response = client.send("GET kappa").decode()
    assert response == "NULL"
