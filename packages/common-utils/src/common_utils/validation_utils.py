"""Validation utility functions."""

import re
from typing import Dict, List, Any


def is_valid_email(email: str) -> bool:
    """Check if an email address is valid.

    Args:
        email: Email address to validate

    Returns:
        True if email is valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_url(url: str) -> bool:
    """Check if a URL is valid.

    Args:
        url: URL to validate

    Returns:
        True if URL is valid, False otherwise
    """
    pattern = r'^https?:\/\/(?:[-\w.])+(?:\:[0-9]+)?(?:\/[^\s]*)?$'
    return re.match(pattern, url) is not None


def validate_required_fields(data: Dict[str, Any], required_fields: List[str]) -> Dict[str, List[str]]:
    """Validate that required fields are present in data.

    Args:
        data: Dictionary containing data to validate
        required_fields: List of field names that are required

    Returns:
        Dictionary with 'errors' key containing list of missing fields
    """
    errors = []
    for field in required_fields:
        if field not in data or data[field] is None or data[field] == "":
            errors.append(f"Field '{field}' is required")

    return {"errors": errors}
