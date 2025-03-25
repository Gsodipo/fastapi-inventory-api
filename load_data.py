import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.inventory_db
collection = db.products

# Load CSV and Convert to JSON
df = pd.read_csv("auto_products.csv")
df = df.rename(columns={"ProductID": "_id"})  # MongoDB uses _id as primary key

# Convert dataframe to dictionary
data = df.to_dict(orient="records")

# Insert into MongoDB
collection.insert_many(data)
print("Data inserted successfully!")
