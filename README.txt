FastAPI API Endpoint Summary
==============================
Generated on: 2025-03-25 13:17:56

GET /getSingleProduct/{product_id}
  Summary: Get Single Product
  Parameters: product_id (path)

GET /getAll
  Summary: Get All
  Parameters: None

POST /addNew
  Summary: Add Product
  Parameters: None

DELETE /deleteOne/{product_id}
  Summary: Delete Product
  Parameters: product_id (path)

GET /startsWith/{letter}
  Summary: Starts With
  Parameters: letter (path)

GET /paginate/{start_id}/{end_id}
  Summary: Paginate
  Parameters: start_id (path), end_id (path)

GET /convert/{product_id}
  Summary: Convert Price
  Parameters: product_id (path)


FastAPI Interactive Docs:
- Swagger UI: http://localhost:8000/docs
- ReDoc:      http://localhost:8000/redoc