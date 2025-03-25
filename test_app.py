from fastapi.testclient import TestClient
from main import app
import uuid  

client = TestClient(app)

def test_add_get_delete_product():
    unique_id = f"AUTO{uuid.uuid4().hex[:6].upper()}"  # e.g. AUTO5F3B2D
    new_product = {
        "Product_ID": unique_id,
        "Name": "Test Product",
        "Unit_Price": 199.99,
        "Stock_Quantity": 10,
        "Description": "A sample test product"
    }

    # Add product
    add_response = client.post("/addNew", json=new_product)
    assert add_response.status_code == 200
    assert add_response.json()["message"] == "Product added successfully"

    # Get product
    get_response = client.get(f"/getSingleProduct/{unique_id}")
    assert get_response.status_code == 200
    assert get_response.json()["Product ID"] == unique_id  # ✅ This fixes the KeyError

    # Delete product
    delete_response = client.delete(f"/deleteOne/{unique_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == f"Product {unique_id} deleted successfully"


# 2. Test fetching all products
def test_get_all():
    response = client.get("/getAll")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 3. Test pagination endpoint
def test_paginate():
    response = client.get("/paginate/1/1000000")  # use large range or add test products
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert isinstance(response.json(), list)

# 4. Test convert price endpoint with known product (update if needed)
def test_convert_price():
    # Either insert a test product with integer _id or skip if not needed
    response = client.get("/convert/1")  # Replace 1 with a valid _id if needed
    assert response.status_code in [200, 404]
