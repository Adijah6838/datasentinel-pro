def test_create_data_source_and_hide_credentials(client):
    # 1. Register and Login
    client.post("/api/v1/auth/register", json={"email": "ds@example.com", "password": "pw", "organization_name": "DS Org"})
    login_res = client.post("/api/v1/auth/login", data={"username": "ds@example.com", "password": "pw"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create Data Source
    response = client.post(
        "/api/v1/data-sources/",
        headers=headers,
        json={
            "name": "My Test DB",
            "source_type": "postgres",
            "config": {"host": "localhost", "password": "supersecret"}
        }
    )
    assert response.status_code == 200
    data = response.json()
    
    # 3. Assertions
    assert data["name"] == "My Test DB"
    assert "config" not in data
    assert "encrypted_config" not in data
    assert "supersecret" not in str(data)