"""
Project B - Data Processing CLI
A command-line tool that demonstrates data processing using shared packages.
"""

import click
import pandas as pd
import json
from datetime import datetime
from decimal import Decimal
from typing import List

# Import from shared packages
from common_utils import (
    capitalize_words,
    slugify,
    format_date,
    is_valid_email,
    validate_required_fields,
    truncate_string
)
from data_models import User, Product, Category, Order, OrderItem, OrderStatus


@click.group()
def cli():
    """Project B - Data Processing CLI Tool"""
    click.echo("🚀 Project B - Data Processing CLI")
    click.echo("Using shared packages: common-utils, data-models")


@cli.command()
@click.option('--input-file', '-i', required=True, help='Input CSV file path')
@click.option('--output-file', '-o', help='Output JSON file path (optional)')
def process_users(input_file, output_file):
    """Process user data from CSV and convert to JSON using shared models."""

    try:
        # Read CSV file
        df = pd.read_csv(input_file)
        click.echo(f"📖 Reading {len(df)} users from {input_file}")

        users = []
        errors = []

        for index, row in df.iterrows():
            try:
                # Validate required fields using shared utility
                required_fields = ['username', 'email', 'first_name', 'last_name']
                row_dict = row.to_dict()
                validation_result = validate_required_fields(row_dict, required_fields)

                if validation_result['errors']:
                    errors.append(f"Row {index + 1}: {', '.join(validation_result['errors'])}")
                    continue

                # Validate email using shared utility
                if not is_valid_email(row['email']):
                    errors.append(f"Row {index + 1}: Invalid email address '{row['email']}'")
                    continue

                # Create User object using shared data model
                user = User(
                    id=index + 1,
                    username=row['username'].lower(),
                    email=row['email'].lower(),
                    first_name=capitalize_words(str(row['first_name'])),
                    last_name=capitalize_words(str(row['last_name'])),
                    is_active=row.get('is_active', True)
                )

                users.append(user.to_dict())
                click.echo(f"✅ Processed user: {user.full_name}")

            except Exception as e:
                errors.append(f"Row {index + 1}: {str(e)}")

        # Display results
        click.echo(f"\n📊 Processing Results:")
        click.echo(f"   ✅ Successfully processed: {len(users)} users")
        click.echo(f"   ❌ Errors: {len(errors)}")

        if errors:
            click.echo("\n🚨 Errors encountered:")
            for error in errors:
                click.echo(f"   - {error}")

        # Save output
        output_data = {
            "processed_at": datetime.now().isoformat(),
            "total_processed": len(users),
            "total_errors": len(errors),
            "users": users
        }

        if output_file:
            with open(output_file, 'w') as f:
                json.dump(output_data, f, indent=2)
            click.echo(f"💾 Output saved to {output_file}")
        else:
            click.echo(f"\n📄 JSON Output:")
            click.echo(json.dumps(output_data, indent=2))

    except Exception as e:
        click.echo(f"❌ Error processing file: {e}")


@cli.command()
@click.option('--input-file', '-i', required=True, help='Input CSV file path')
@click.option('--output-file', '-o', help='Output JSON file path (optional)')
def process_products(input_file, output_file):
    """Process product data from CSV and convert to JSON using shared models."""

    try:
        df = pd.read_csv(input_file)
        click.echo(f"📖 Reading {len(df)} products from {input_file}")

        products = []
        errors = []

        for index, row in df.iterrows():
            try:
                # Validate required fields
                required_fields = ['name', 'description', 'price', 'sku', 'category_id']
                row_dict = row.to_dict()
                validation_result = validate_required_fields(row_dict, required_fields)

                if validation_result['errors']:
                    errors.append(f"Row {index + 1}: {', '.join(validation_result['errors'])}")
                    continue

                # Create Product object using shared data model
                product = Product(
                    id=index + 1,
                    name=capitalize_words(str(row['name'])),
                    description=truncate_string(str(row['description']), 200),
                    price=Decimal(str(row['price'])),
                    sku=str(row['sku']).upper(),
                    category_id=int(row['category_id']),
                    stock_quantity=int(row.get('stock_quantity', 0)),
                    tags=[tag.strip() for tag in str(row.get('tags', '')).split(',') if tag.strip()]
                )

                products.append(product.to_dict())
                click.echo(f"✅ Processed product: {product.name} (${product.price})")

            except Exception as e:
                errors.append(f"Row {index + 1}: {str(e)}")

        # Display results
        click.echo(f"\n📊 Processing Results:")
        click.echo(f"   ✅ Successfully processed: {len(products)} products")
        click.echo(f"   ❌ Errors: {len(errors)}")

        if errors:
            click.echo("\n🚨 Errors encountered:")
            for error in errors:
                click.echo(f"   - {error}")

        # Save output
        output_data = {
            "processed_at": datetime.now().isoformat(),
            "total_processed": len(products),
            "total_errors": len(errors),
            "products": products
        }

        if output_file:
            with open(output_file, 'w') as f:
                json.dump(output_data, f, indent=2)
            click.echo(f"💾 Output saved to {output_file}")
        else:
            click.echo(f"\n📄 JSON Output:")
            click.echo(json.dumps(output_data, indent=2))

    except Exception as e:
        click.echo(f"❌ Error processing file: {e}")


@cli.command()
@click.argument('text')
def text_utils(text):
    """Demonstrate text utilities from shared package."""

    click.echo(f"🔧 Text Utilities Demo")
    click.echo(f"Original text: '{text}'")
    click.echo(f"")

    # Capitalize
    capitalized = capitalize_words(text)
    click.echo(f"Capitalized:   '{capitalized}'")

    # Slugify
    slug = slugify(text)
    click.echo(f"Slugified:     '{slug}'")

    # Truncate
    truncated = truncate_string(text, 20)
    click.echo(f"Truncated:     '{truncated}'")


@cli.command()
@click.argument('email')
def validate_email_cmd(email):
    """Validate an email address using shared utilities."""

    is_valid = is_valid_email(email)
    status = "✅ Valid" if is_valid else "❌ Invalid"

    click.echo(f"📧 Email Validation")
    click.echo(f"Email: {email}")
    click.echo(f"Status: {status}")


@cli.command()
def generate_sample_data():
    """Generate sample CSV files for testing."""

    # Generate sample users CSV
    users_data = [
        {"username": "john_doe", "email": "john.doe@example.com", "first_name": "john", "last_name": "doe", "is_active": True},
        {"username": "jane_smith", "email": "jane.smith@example.com", "first_name": "jane", "last_name": "smith", "is_active": True},
        {"username": "bob_wilson", "email": "bob.wilson@example.com", "first_name": "bob", "last_name": "wilson", "is_active": False},
        {"username": "invalid_user", "email": "invalid-email", "first_name": "test", "last_name": "user", "is_active": True},  # Invalid email for testing
    ]

    df_users = pd.DataFrame(users_data)
    df_users.to_csv('sample_users.csv', index=False)
    click.echo("📄 Generated sample_users.csv")

    # Generate sample products CSV
    products_data = [
        {"name": "smartphone pro", "description": "Latest smartphone with advanced features and great camera", "price": 699.99, "sku": "PHONE-001", "category_id": 1, "stock_quantity": 50, "tags": "electronics,mobile,smartphone"},
        {"name": "laptop ultrabook", "description": "Lightweight laptop perfect for professionals", "price": 1299.99, "sku": "LAPTOP-001", "category_id": 1, "stock_quantity": 25, "tags": "electronics,computer,laptop"},
        {"name": "python cookbook", "description": "Comprehensive guide to Python programming with practical examples", "price": 39.99, "sku": "BOOK-001", "category_id": 2, "stock_quantity": 100, "tags": "books,programming,python"},
        {"name": "wireless headphones", "description": "High-quality wireless headphones with noise cancellation", "price": 199.99, "sku": "AUDIO-001", "category_id": 1, "stock_quantity": 75, "tags": "electronics,audio,headphones"},
    ]

    df_products = pd.DataFrame(products_data)
    df_products.to_csv('sample_products.csv', index=False)
    click.echo("📄 Generated sample_products.csv")

    click.echo("\n✨ Sample files generated successfully!")
    click.echo("Try running:")
    click.echo("  python cli.py process-users -i sample_users.csv")
    click.echo("  python cli.py process-products -i sample_products.csv")


@cli.command()
def demo():
    """Run a complete demonstration of shared package capabilities."""

    click.echo("🎉 Demo: Shared Package Integration")
    click.echo("=" * 50)

    # Create sample data using shared models
    click.echo("\n1. Creating sample data using shared models...")

    # Create a user
    user = User(
        id=1,
        username="demo_user",
        email="demo@example.com",
        first_name="demo",
        last_name="user"
    )
    click.echo(f"   User created: {user.full_name}")

    # Create a product
    product = Product(
        id=1,
        name="demo product",
        description="A sample product for demonstration",
        price=Decimal("99.99"),
        sku="DEMO-001",
        category_id=1,
        stock_quantity=10
    )
    click.echo(f"   Product created: {product.name} ({product.formatted_price})")

    # Create an order
    order = Order(
        id=1,
        user_id=user.id,
        status=OrderStatus.PENDING
    )

    order_item = OrderItem(
        id=1,
        product_id=product.id,
        product_name=product.name,
        product_sku=product.sku,
        quantity=2,
        unit_price=product.price
    )

    order.add_item(order_item)
    click.echo(f"   Order created: {order.total_items} items, {order.formatted_total_amount}")

    # Demonstrate utilities
    click.echo("\n2. Testing utility functions...")

    sample_text = "hello world example"
    click.echo(f"   Original: '{sample_text}'")
    click.echo(f"   Capitalized: '{capitalize_words(sample_text)}'")
    click.echo(f"   Slugified: '{slugify(sample_text)}'")
    click.echo(f"   Truncated: '{truncate_string(sample_text, 15)}'")

    sample_email = "test@example.com"
    click.echo(f"   Email '{sample_email}' is valid: {is_valid_email(sample_email)}")

    current_time = datetime.now()
    click.echo(f"   Current time: {format_date(current_time, '%Y-%m-%d %H:%M:%S')}")

    click.echo("\n✅ Demo completed successfully!")


if __name__ == '__main__':
    cli()
