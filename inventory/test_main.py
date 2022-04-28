'''Main test file'''
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_all_products():
    '''Should return a 200 status code if running correctly.'''
    response = client.get('/products')
    assert response.status_code == 200


def test_get_non_existent_product():
    '''Should return a 404 status code when trying to delete a product with non-existent pk.'''
    response = client.get('/products/NONEXISTNT_PK')
    assert response.status_code == 404
