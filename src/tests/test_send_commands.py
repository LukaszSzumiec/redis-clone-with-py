def test_first_message(tcp_server, client):
    response = client.send("Test")
    assert "Received" == response.decode()


def test_set_message(tcp_server, client):
    response = client.send("SET kappa 1").decode()
    assert "OK" == response

    response = client.send("GET kappa").decode()
    assert "1" == response
