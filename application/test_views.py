import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    response = client.get('/index')
    assert response.status_code == 200
    assert b'Home' in response.data

def test_test_script(client):
    response = client.get('/test_script.html')
    assert response.status_code == 200

def test_fib_usage(client):
    response = client.get('/fib/')
    assert response.status_code == 200

def test_my_fib(client):
    response = client.get('/fib/10')
    assert response.status_code == 200
    assert b'Fibonacci sequence' in response.data

def test_my_fib_invalid_input(client):
    response = client.get('/fib/abc')
    assert response.status_code == 200
    assert b'Invalid input' in response.data

def test_my_fib_negative_input(client):
    response = client.get('/fib/-10')
    assert response.status_code == 200
    assert b'Invalid input' in response.data

def test_my_fib_large_input(client):
    response = client.get('/fib/1000')
    assert response.status_code == 200
    assert b'Fibonacci sequence' in response.data
