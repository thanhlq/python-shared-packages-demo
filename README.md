# Python Shared Packages Demo

A demonstration workspace showing how to structure and use shared Python packages across multiple projects.

## 📁 Workspace Structure

```
my-workspace/
├── shared-packages/
│   ├── common-utils/                 # Shared utility functions
│   │   ├── setup.py                 # Package configuration
│   │   └── src/common_utils/        # Source code
│   │       ├── __init__.py          # Package initialization
│   │       ├── string_utils.py      # String manipulation utilities
│   │       ├── date_utils.py        # Date/time utilities
│   │       ├── validation_utils.py  # Validation functions
│   │       └── config_utils.py      # Configuration utilities
│   └── data-models/                 # Shared data models
│       ├── setup.py                 # Package configuration
│       └── src/data_models/         # Source code
│           ├── __init__.py          # Package initialization
│           ├── user.py              # User models
│           ├── product.py           # Product models
│           └── order.py             # Order models
├── project-a/                       # Flask Web API Service
│   ├── Pipfile                     # Dependencies with shared packages
│   ├── README.md                   # Project-specific documentation
│   └── src/
│       └── app.py                  # Flask application
└── project-b/                      # Data Processing CLI
    ├── Pipfile                     # Dependencies with shared packages
    ├── README.md                   # Project-specific documentation
    └── src/
        └── cli.py                  # CLI application
```

## 🚀 Quick Start

### 1. Clone and Navigate
```bash
cd python-shared-packages-demo
```

### 2. Install Shared Packages (Development Mode)
Install the shared packages in development mode so changes are immediately available:

```bash
# Install common-utils package
cd shared-packages/common-utils
pip install -e .
cd ../..

# Install data-models package
cd shared-packages/data-models
pip install -e .
cd ../..
```

### 3. Set Up Project A (Flask Web API)
```bash
cd project-a
pipenv install
pipenv shell
cd src
pipenv run python app.py
```
Access the API at http://localhost:5001

### 4. Set Up Project B (CLI Tool)
```bash
cd project-b
pipenv install
pipenv shell
cd src
python cli.py demo
```

## 📦 Shared Packages

### common-utils
Provides utility functions for common operations:

- **String Utils**: `capitalize_words()`, `slugify()`, `truncate_string()`
- **Date Utils**: `format_date()`, `parse_date()`, `days_between()`
- **Validation Utils**: `is_valid_email()`, `is_valid_url()`, `validate_required_fields()`
- **Config Utils**: `get_env_var()`, `load_config()`

### data-models
Provides data classes for consistent data structures:

- **User Models**: `User`, `UserProfile`
- **Product Models**: `Product`, `Category`
- **Order Models**: `Order`, `OrderItem`, `OrderStatus`

## 🎯 Project Examples

### Project A: Flask Web API Service
- **Purpose**: REST API demonstrating shared package usage
- **Framework**: Flask
- **Features**:
  - User management endpoints
  - Product and category management
  - Order processing
  - Utility endpoints exposing shared functions

**Example API calls:**
```bash
# Get all users
curl http://localhost:5001/users

# Create user with validation
curl -X POST http://localhost:5001/users \
  -H "Content-Type: application/json" \
  -d '{"username": "jane", "email": "jane@example.com", "first_name": "jane", "last_name": "smith"}'

# Test utilities
curl http://localhost:5001/utils/capitalize/hello%20world
curl http://localhost:5001/utils/validate-email/test@example.com
```

### Project B: Data Processing CLI
- **Purpose**: Command-line tool for data processing
- **Framework**: Click
- **Features**:
  - CSV to JSON conversion
  - Data validation and transformation
  - Utility function demonstrations
  - Sample data generation

**Example CLI commands:**
```bash
# Generate sample data
python cli.py generate-sample-data

# Process users with validation
python cli.py process-users -i sample_users.csv -o users.json

# Test text utilities
python cli.py text-utils "hello world example"

# Run complete demo
python cli.py demo
```

## 🛠 Development Workflow

### Adding New Shared Functionality

1. **Add to shared package:**
   ```bash
   cd shared-packages/common-utils/src/common_utils
   # Edit or add new utility modules
   ```

2. **Update package exports:**
   ```python
   # In __init__.py
   from .new_module import new_function
   __all__.append("new_function")
   ```

3. **Use in projects:**
   ```python
   from common_utils import new_function
   ```

### Installing New Dependencies

For shared packages:
```bash
cd shared-packages/common-utils
# Edit setup.py to add dependencies
pip install -e .  # Reinstall in development mode
```

For individual projects:
```bash
cd project-a
pipenv install new-package
```

## 🧪 Testing

### Testing Shared Packages
```bash
cd shared-packages/common-utils
python -m pytest tests/
```

### Testing Projects
```bash
cd project-a
pipenv shell
python -m pytest

cd ../project-b
pipenv shell
python -m pytest
```

## 📚 Key Benefits

1. **Code Reusability**: Write once, use everywhere
2. **Consistency**: Shared models ensure data consistency
3. **Maintainability**: Central location for common functionality
4. **Scalability**: Easy to add new projects that use shared packages
5. **Development Efficiency**: No code duplication across projects
6. **Modularity** Not needed for recurrent tests of untouched package

## 🔗 Dependencies Management

The workspace uses:
- **Pipenv** for project-level dependency management
- **Editable installs** (`-e`) for development mode shared packages
- **Local path references** in Pipfile for shared packages

Example Pipfile entry:
```toml
[packages]
common-utils = {path = "../shared-packages/common-utils", editable = true}
data-models = {path = "../shared-packages/data-models", editable = true}
```

## 🎮 Try It Out

1. **Start the API service:**
   ```bash
   cd project-a && pipenv shell && cd src && python app.py
   ```

2. **In another terminal, try the CLI tool:**
   ```bash
   cd project-b && pipenv shell && cd src && python cli.py demo
   ```

3. **Test API endpoints:**
   ```bash
   curl http://localhost:5001/
   curl http://localhost:5001/utils/slugify/Hello%20World
   ```

4. **Process some data:**
   ```bash
   cd project-b/src
   python cli.py generate-sample-data
   python cli.py process-users -i sample_users.csv
   ```

This demonstrates a complete shared package ecosystem for Python development! 🎉
