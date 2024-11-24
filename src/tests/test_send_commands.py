def test_first_message(tcp_server, quick_client):
    response = quick_client.connect_and_send("Test")
    assert response.decode() == "Syntax Error"


def test_set_call(tcp_server, quick_client):
    response = quick_client.connect_and_send("SET kappa 1").decode()
    assert response == "OK"

    response = quick_client.connect_and_send("GET kappa").decode()
    assert response == "1"


def test_delete_call(tcp_server, quick_client):
    response = quick_client.connect_and_send("SET kappa 1").decode()
    assert response == "OK"

    response = quick_client.connect_and_send("DEL kappa").decode()
    assert response == "Deleted"

    response = quick_client.connect_and_send("GET kappa").decode()
    assert response == "NULL"


def test_two_clients(tcp_server, separated_client):
    with separated_client() as client_1:
        with separated_client() as client_2:
            response = client_1.send("SET kappa 1").decode()
            assert response == "OK"

            response = client_2.send("GET kappa").decode()
            assert response == "1"

            response = client_2.send("SET kappa 2").decode()
            assert response == "OK"

            response = client_1.send("GET kappa").decode()
            assert response == "2"
