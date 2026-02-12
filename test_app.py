import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b"api is working "

def test_add(client):
    response = client.post('/add', json={'a': 5, 'b': 3})
    assert response.status_code == 200
    assert response.get_json() == {"result": 8}

def test_add_invalid(client):
    response = client.post('/add', json={'a': '5', 'b': 3})
    assert response.status_code == 400
# class FlaskAppTestCase(unittest.TestCase):
#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_hello(self):
#         response = self.app.get('/hello')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.get_json(), {"message": "Hello, World!"})

#     def test_add(self):
#         response = self.app.post('/add', json={'a': 5, 'b': 3})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.get_json(), {"result": 8})

# if __name__ == '__main__':
#     unittest.main()