"""
Module to test URL parsing.
"""

import urllib.parse
import pytest
from utils import parse_url


def test_parse_url_valid():
    """
    Test parsing a valid URL.
    """
    url = "https://www.example.com/path?query#fragment"
    expected_components = urllib.parse.urlparse(url)
    assert parse_url(url) == expected_components


def test_parse_url_invalid():
    """
    Test parsing an invalid URL.
    """
    url = "invalid_url"
    with pytest.raises(ValueError):
        parse_url(url)
