def test_client(client):
    rv = client.get("/alive")
    assert rv.status_code == 200