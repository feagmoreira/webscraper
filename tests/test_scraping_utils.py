"""
Test Cases for scraping utils functions from utils package
"""
import pytest

import webscraper.utils.scraping_utils as scraping_utils

# validate_url tests
def test_validate_url_valid_url():
    url = "https://livetopia-party.en.aptoide.com/app"
    result = scraping_utils.validate_url(url)
    assert result == True

def test_validate_url_invalid_url():
    url = "x"
    result = scraping_utils.validate_url(url)
    assert result == False

def test_validate_url_empty_url():
    url = ""
    result = scraping_utils.validate_url(url)
    assert result == False

# get_html_page tests

def test_get_html_page_valid_format_valid_url():
    url = "https://livetopia-party.en.aptoide.com/app"
    result = scraping_utils.get_html_page(url)
    assert "Error getting html" not in result

def test_get_html_page_valid_format_invalid_url():
    url = "https://livetopia-party.en.aptoide.com/appWW"
    result = scraping_utils.get_html_page(url)
    assert "Error getting html" in result

def test_get_html_page_invalid_format_invalid_url():
    url = "x"
    result = scraping_utils.get_html_page(url)
    assert "Error getting html" in result