"""
Project A - Web API Service
A Flask web service that demonstrates the use of shared packages.
"""

from common_utils.aim import iam_get_user_roles
from flask import Flask, jsonify, request
from datetime import datetime
from decimal import Decimal

# Import from shared packages
from common_utils import capitalize_words, slugify, format_date, is_valid_email
from data_models import User, Product, Category, Order, OrderItem, OrderStatus

app = Flask(__name__)

# Sample data storage (in real apps, this would be a database)
users = {}
products = {}
categories = {}
orders = {}

# Initialize some sample data
def init_sample_data():
    """Initialize some sample data for demonstration."""

    # Create categories
    categories[1] = Category(
        id=1,
        name="Electronics",
        description="Electronic devices and accessories"
    )

    categories[2] = Category(
        id=2,
        name="Books",
        description="Books and educational materials"
    )

    # Create products
    products[1] = Product(
        id=1,
        name="Smartphone",
        description="Latest smartphone with advanced features",
        price=Decimal("699.99"),
        sku="PHONE-001",
        category_id=1,
        stock_quantity=50,
        tags=["electronics", "mobile", "smartphone"]
    )

    products[2] = Product(
        id=2,
        name="Python Programming Book",
        description="Comprehensive guide to Python programming",
        price=Decimal("39.99"),
        sku="BOOK-001",
        category_id=2,
        stock_quantity=100,
        tags=["books", "programming", "python"]
    )

    # Create users
    users[1] = User(
        id=1,
        username="johndoe",
        email="john.doe@example.com",
        first_name="John 2",
        last_name="Doe"
    )

    print("Sample data initialized!")


@app.route('/')
def home():
    """Home endpoint with API information."""
    return jsonify({
        "message": "Welcome to Project A - Web API Service",
        "description": "This service demonstrates shared package usage",
        "endpoints": [
            "/users",
            "/users/<id>",
            "/products",
            "/products/<id>",
            "/categories",
            "/orders",
            "/orders/<id>",
            "/utils/capitalize/<text>",
            "/utils/slugify/<text>",
            "/utils/validate-email/<email>"
        ]
    })

@app.route('/roles', methods=['GET', 'POST'])
def handle_roles():
    """Handle role operations."""
    if request.method == 'GET':
        return jsonify(iam_get_user_roles())

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    """Handle user operations."""
    if request.method == 'GET':
        return jsonify([user.to_dict() for user in users.values()])

    if request.method == 'POST':
        data = request.get_json()

        # Validate required fields
        required_fields = ['username', 'email', 'first_name', 'last_name']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {missing_fields}"}), 400

        # Validate email using shared utility
        if not is_valid_email(data['email']):
            return jsonify({"error": "Invalid email address"}), 400

        # Create new user
        user_id = len(users) + 1
        user = User(
            id=user_id,
            username=data['username'],
            email=data['email'],
            first_name=capitalize_words(data['first_name']),
            last_name=capitalize_words(data['last_name'])
        )

        users[user_id] = user
        return jsonify(user.to_dict()), 201


@app.route('/users/<int:user_id>')
def get_user(user_id):
    """Get a specific user."""
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())


@app.route('/products')
def get_products():
    """Get all products."""
    return jsonify([product.to_dict() for product in products.values()])


@app.route('/products/<int:product_id>')
def get_product(product_id):
    """Get a specific product."""
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.to_dict())


@app.route('/categories')
def get_categories():
    """Get all categories."""
    return jsonify([category.to_dict() for category in categories.values()])


@app.route('/orders', methods=['GET', 'POST'])
def handle_orders():
    """Handle order operations."""
    if request.method == 'GET':
        return jsonify([order.to_dict() for order in orders.values()])

    if request.method == 'POST':
        data = request.get_json()

        # Create new order
        order_id = len(orders) + 1
        order = Order(
            id=order_id,
            user_id=data['user_id'],
            status=OrderStatus.PENDING,
            shipping_address=data.get('shipping_address'),
            billing_address=data.get('billing_address')
        )

        # Add items to order
        for item_data in data.get('items', []):
            product = products.get(item_data['product_id'])
            if product:
                order_item = OrderItem(
                    id=len(order.items) + 1,
                    product_id=product.id,
                    product_name=product.name,
                    product_sku=product.sku,
                    quantity=item_data['quantity'],
                    unit_price=product.price
                )
                order.add_item(order_item)

        orders[order_id] = order
        return jsonify(order.to_dict()), 201


@app.route('/orders/<int:order_id>')
def get_order(order_id):
    """Get a specific order."""
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict())


# Utility endpoints demonstrating shared package functions
@app.route('/utils/capitalize/<text>')
def capitalize_text(text):
    """Capitalize text using shared utility."""
    return jsonify({
        "original": text,
        "capitalized": capitalize_words(text)
    })


@app.route('/utils/slugify/<text>')
def slugify_text(text):
    """Slugify text using shared utility."""
    return jsonify({
        "original": text,
        "slugified": slugify(text)
    })


@app.route('/utils/validate-email/<email>')
def validate_email(email):
    """Validate email using shared utility."""
    return jsonify({
        "email": email,
        "is_valid": is_valid_email(email)
    })


@app.route('/utils/current-time')
def current_time():
    """Get current time formatted using shared utility."""
    now = datetime.now()
    return jsonify({
        "timestamp": now.isoformat(),
        "formatted_date": format_date(now),
        "formatted_datetime": format_date(now, "%Y-%m-%d %H:%M:%S")
    })


if __name__ == '__main__':
    init_sample_data()
    print("Starting Project A - Web API Service...")
    print("Shared packages: common-utils, data-models")
    app.run(host='0.0.0.0', port=5001, debug=True)
