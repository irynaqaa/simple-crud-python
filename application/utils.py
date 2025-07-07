"""
Module to parse URLs.
"""

import urllib.parse


def parse_url(url):
    """
    Parse a URL and return its components.

    Args:
        url (str): The URL to parse.

    Returns:
        urllib.parse.ParseResult: The parsed URL components.

    Raises:
        ValueError: If the URL is invalid.
    """
    try:
        return urllib.parse.urlparse(url)
    except ValueError as exc:
        raise ValueError("Invalid URL") from exc
