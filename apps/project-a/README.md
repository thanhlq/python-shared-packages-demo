# Project A

A Flask web API service that demonstrates the use of shared packages.

## Setup

1. Install dependencies:
   ```bash
   pipenv install
   ```

2. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

3. Run the application:
   ```bash
   cd src
   python app.py
   ```

## Features

This project demonstrates:

- **Shared Utilities**: Uses `common-utils` package for string manipulation, validation, and date formatting
- **Shared Data Models**: Uses `data-models` package for User, Product, Category, and Order models
- **REST API**: Provides endpoints for managing users, products, categories, and orders
- **Utility Endpoints**: Exposes shared utility functions via HTTP endpoints

## API Endpoints

### Core Resources
- `GET /` - API information
- `GET/POST /users` - User management
- `GET /users/<id>` - Get specific user
- `GET /products` - List products
- `GET /products/<id>` - Get specific product
- `GET /categories` - List categories
- `GET/POST /orders` - Order management
- `GET /orders/<id>` - Get specific order

### Utility Endpoints
- `GET /utils/capitalize/<text>` - Capitalize text
- `GET /utils/slugify/<text>` - Convert text to URL slug
- `GET /utils/validate-email/<email>` - Validate email address
- `GET /utils/current-time` - Get formatted current time

## Example Usage

```bash
# Get all users
curl http://localhost:5001/users

# Create a user
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{"username": "jane", "email": "jane@example.com", "first_name": "jane", "last_name": "smith"}'

# Test utility functions
curl http://localhost:5001/utils/capitalize/hello%20world
curl http://localhost:5001/utils/slugify/Hello%20World%20Example
curl http://localhost:5001/utils/validate-email/test@example.com
```
