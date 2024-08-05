def test_user_register(client):
    user_1 = {
        "data": {
            "username": "admin",
            "email": "email_test@admin.com",
            "password": "ab@A1234567"
        }
    }
    response_1 = client.post('/api/users/register', json=user_1)
    print(response_1.data)
    assert response_1.status_code == 201

    # username duplicate
    user_2 = {
        "data": {
            "username": "admin",
            "email": "email_test2@admin.com",
            "password": "ab@A1234567"
        }
    }
    response_2 = client.post('/api/users/register', json=user_2)
    print(response_2.data)
    assert response_2.status_code == 400

    # password not meet requirement
    user_3 = {
        "data": {
            "username": "admin2",
            "email": "email_test2@admin.com",
            "password": "ab@A12"
        }
    }
    response_3 = client.post('/api/users/register', json=user_3)
    print(response_3.data)
    assert response_3.status_code == 400
