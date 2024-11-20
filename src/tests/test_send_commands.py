def test_first_message(tcp_server, client):
    response = client.send("Test")
    assert "Received" == response.decode()
