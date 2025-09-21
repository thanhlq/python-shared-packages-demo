"""Date and time utility functions."""

from datetime import datetime, date
from dateutil import parser
from dateutil.relativedelta import relativedelta


def format_date(date_obj, format_string: str = "%Y-%m-%d") -> str:
    """Format a date object to string.

    Args:
        date_obj: A datetime or date object
        format_string: The format string for the output

    Returns:
        Formatted date string
    """
    if isinstance(date_obj, (datetime, date)):
        return date_obj.strftime(format_string)
    raise TypeError("date_obj must be a datetime or date object")


def parse_date(date_string: str):
    """Parse a date string into a datetime object.

    Args:
        date_string: A string representation of a date

    Returns:
        datetime object
    """
    return parser.parse(date_string)


def days_between(start_date, end_date) -> int:
    """Calculate the number of days between two dates.

    Args:
        start_date: Start date (datetime or date object)
        end_date: End date (datetime or date object)

    Returns:
        Number of days between the dates
    """
    if isinstance(start_date, datetime):
        start_date = start_date.date()
    if isinstance(end_date, datetime):
        end_date = end_date.date()

    return (end_date - start_date).days
