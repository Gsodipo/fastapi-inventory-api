from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel, Field, ConfigDict
import requests
import os
from dotenv import load_dotenv
from bson import ObjectId  # Import for handling ObjectId in MongoDB


load_dotenv()

app = FastAPI()

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.inventory_db
collection = db.products


class Product(BaseModel):
    Product_ID: str = Field(..., alias="Product ID")
    Name: str
    Unit_Price: float = Field(..., alias="Unit Price")
    Stock_Quantity: int = Field(..., alias="Stock Quantity")
    Description: str

    model_config = ConfigDict(populate_by_name=True)  # 👈 new way to allow using field names

# 1. Get single product by ID
@app.get("/getSingleProduct/{product_id}")
def get_single_product(product_id: str):  # Keep product_id as string
    product = collection.find_one({"Product ID": product_id}, {"_id": 0})  # Search in "Product ID" field
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# 2. Get all products
@app.get("/getAll")
def get_all():
    return list(collection.find({}, {"_id": 0}))

# 3. Add a new product
@app.post("/addNew")
def add_product(product: Product):
    # Check if the product already exists
    if collection.find_one({"Product_ID": product.Product_ID}):
        raise HTTPException(status_code=400, detail="Product with this ID already exists")

    # Insert product into MongoDB
    collection.insert_one(product.model_dump(by_alias=True))

    return {"message": "Product added successfully", "product": product}


# 4. Delete a product by ID
@app.delete("/deleteOne/{product_id}")
def delete_product(product_id: str):  # Ensure product_id is a string
    result = collection.delete_one({"Product ID": product_id})  # Match the MongoDB field name

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")

    return {"message": f"Product {product_id} deleted successfully"}



# 5. Find products that start with a letter
@app.get("/startsWith/{letter}")
def starts_with(letter: str):
    return list(collection.find({"Name": {"$regex": f"^{letter}", "$options": "i"}}, {"_id": 0}))

# 6. Paginate products
@app.get("/paginate/{start_id}/{end_id}")
def paginate(start_id: str, end_id: str):
    products = list(collection.find(
        {"Product ID": {"$gte": start_id, "$lte": end_id}},  # Match "Product ID" as a string
        {"_id": 0}  # Exclude MongoDB ObjectId
    ).sort("Product ID", 1).limit(10))  # Sort in ascending order

    if not products:
        raise HTTPException(status_code=404, detail="No products found in this range")

    return products


# 7. Convert product price from USD to EUR
@app.get("/convert/{product_id}")
def convert_price(product_id: str):  # Change product_id to string
    product = collection.find_one({"Product ID": product_id})  # Match "Product ID" field
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    exchange_rate = response.json()["rates"]["EUR"]
    converted_price = product["Unit Price"] * exchange_rate  # Fix key to "Unit Price"
    
    return {
        "Product": product["Name"],
        "Price in EUR": round(converted_price, 2)
    }

