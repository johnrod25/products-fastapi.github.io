import requests

Endpoint = "http://127.0.0.1:8000"

def test_add_product():
    payload = {
        "name": "product",
        "description": "descccc",
        "price": 3432
    }
    add_response = requests.post(Endpoint+"/add-product/", json=payload)
    assert add_response.status_code == 201

def test_list_products():
    list_product_response = requests.get(Endpoint+"/products")
    assert list_product_response.status_code == 200
    data = list_product_response.json()
    #print(data)

def test_read_product():
    product_id = 1
    read_product_reponse = requests.get(Endpoint+f"/products/{product_id}")
    assert read_product_reponse.status_code == 200
    data = read_product_reponse.json()
    #print(data)

def test_update_product():
    payload = {
        "name": "product11",
        "description": "product updated",
        "price": 12234
    }
    product_id = 1
    update_product_reponse = requests.put(Endpoint+f"/update-product/{product_id}", json=payload)
    assert update_product_reponse.status_code == 200
    data = update_product_reponse.json()
    #print(data)

def test_delete_product():
    product_id = 26
    delete_product_response = requests.delete(Endpoint+f"/delete-product/{product_id}")
    assert delete_product_response.status_code == 200
    data = delete_product_response.json()
    #print(data)