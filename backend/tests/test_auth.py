def test_register_user(client):
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "testpassword", "organization_name": "Test Org"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["role"] == "admin"

def test_login_user(client):
    # Register first
    client.post(
        "/api/v1/auth/register",
        json={"email": "login@example.com", "password": "testpassword", "organization_name": "Login Org"}
    )
    # Login
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "login@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"