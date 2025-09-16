"""Common utilities package for shared functionality across projects."""

from .string_utils import capitalize_words, slugify, truncate_string
from .date_utils import format_date, parse_date, days_between
from .validation_utils import is_valid_email, is_valid_url, validate_required_fields
from .config_utils import load_config, get_env_var

__version__ = "0.1.0"
__all__ = [
    "capitalize_words",
    "slugify",
    "truncate_string",
    "format_date",
    "parse_date",
    "days_between",
    "is_valid_email",
    "is_valid_url",
    "validate_required_fields",
    "load_config",
    "get_env_var",
]
