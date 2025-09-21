"""Configuration and environment utility functions."""

import os
import json
from typing import Any, Optional, Dict


def get_env_var(name: str, default: Optional[str] = None, required: bool = False) -> str:
    """Get an environment variable value.

    Args:
        name: Name of the environment variable
        default: Default value if variable is not set
        required: Whether the variable is required

    Returns:
        Value of the environment variable

    Raises:
        ValueError: If required variable is not set
    """
    value = os.getenv(name, default)
    if required and value is None:
        raise ValueError(f"Required environment variable '{name}' is not set")
    return value


def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from a JSON file.

    Args:
        config_path: Path to the configuration file

    Returns:
        Dictionary containing configuration data

    Raises:
        FileNotFoundError: If config file doesn't exist
        json.JSONDecodeError: If config file contains invalid JSON
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, 'r') as f:
        return json.load(f)
