import os
import json
import zipfile
from datetime import datetime
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]
collection = db["products"]  # Use your collection name

# Fetch all product records
products = list(collection.find({}, {"_id": 0}))  # exclude MongoDB _id

# Create a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Set filenames
json_filename = f"product_dump_{timestamp}.json"
zip_filename = f"database-{timestamp}.zip"

# Save JSON dump
with open(json_filename, "w") as f:
    json.dump(products, f, indent=4)

# Create ZIP archive
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(json_filename)

# Clean up JSON file
os.remove(json_filename)

print(f"✅ Created ZIP file: {zip_filename}")
