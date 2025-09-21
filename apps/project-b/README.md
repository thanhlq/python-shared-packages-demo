# Project B

A command-line data processing tool that demonstrates the use of shared packages.

## Setup

1. Install dependencies:

   ```bash
   pipenv install
   ```

2. Activate the virtual environment:

   ```bash
   pipenv shell
   ```

3. Run the CLI tool:

   ```bash
   cd src
   python cli.py --help
   ```

## Features

This project demonstrates:

- **Shared Utilities**: Uses `common-utils` package for string processing, validation, and formatting
- **Shared Data Models**: Uses `data-models` package for structured data handling
- **Data Processing**: CSV to JSON conversion with validation
- **CLI Interface**: Command-line interface using Click

## Commands

### Core Commands

- `python cli.py demo` - Run a complete demonstration
- `python cli.py generate-sample-data` - Create sample CSV files for testing
- `python cli.py process-users -i <csv_file>` - Process user data from CSV
- `python cli.py process-products -i <csv_file>` - Process product data from CSV

### Utility Commands

- `python cli.py text-utils <text>` - Demonstrate text processing utilities
- `python cli.py validate-email-cmd <email>` - Validate email addresses

## Example Usage

```bash
# Generate sample data
python cli.py generate-sample-data

# Process users from CSV
python cli.py process-users -i sample_users.csv -o users_output.json

# Process products from CSV
python cli.py process-products -i sample_products.csv -o products_output.json

# Test text utilities
python cli.py text-utils "hello world example"

# Validate email
python cli.py validate-email-cmd "test@example.com"

# Run full demo
python cli.py demo
```

## Sample Data Format

### Users CSV Format
```csv
username,email,first_name,last_name,is_active
john_doe,john.doe@example.com,john,doe,True
jane_smith,jane.smith@example.com,jane,smith,True
```

### Products CSV Format
```csv
name,description,price,sku,category_id,stock_quantity,tags
smartphone pro,Latest smartphone with advanced features,699.99,PHONE-001,1,50,"electronics,mobile,smartphone"
python cookbook,Comprehensive guide to Python programming,39.99,BOOK-001,2,100,"books,programming,python"
```

## Data Processing Features

- **Validation**: Uses shared utilities to validate required fields and email addresses
- **Data Transformation**: Capitalizes names, formats SKUs, processes tags
- **Error Handling**: Collects and reports processing errors
- **Output Formatting**: Generates structured JSON output with metadata
