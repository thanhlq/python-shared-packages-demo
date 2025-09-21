"""String utility functions."""

import re


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word in the text.

    Args:
        text: The input text to capitalize

    Returns:
        The text with each word capitalized
    """
    return text.title()


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug.

    Args:
        text: The input text to slugify

    Returns:
        A lowercase, hyphenated version of the text
    """
    # Remove special characters and replace spaces with hyphens
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')


def truncate_string(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate a string to a maximum length.

    Args:
        text: The input text to truncate
        max_length: Maximum length of the resulting string
        suffix: Suffix to append when text is truncated

    Returns:
        The truncated text with suffix if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
