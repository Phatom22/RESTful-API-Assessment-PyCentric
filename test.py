import pytest
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

#test for retrieving the list
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Jefferson", "email":"jeffersonphato@gmail.com"},
                               {"id": 2, "name": "John", "email":"john@gmail.com"}
                               ]

#test for retrievings specific user
def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jefferson", "email":"jeffersonphato@gmail.com"}

#test for create new user
def test_create_user():
    response = client.post("/users",json={"id":3,"name":"Tau","email":"tau@gmail.com"})
    assert response.status_code == 200
    assert response.json() == {"id":3,"name":"Tau","email":"tau@gmail.com"}

#test for updating user
#def test_upa   
#test for for 
def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {'message': 'user has been deleted'}

