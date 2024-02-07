"""
Test Cases for function test_extract_ApptoidApp_from_html from resource package
"""
import pytest

import webscraper.resources.aptoide as aptoide_resource
import webscraper.model.aptoide as aptoide_model
import webscraper.utils.scraping_utils as scraping_utils

def test_extract_ApptoidApp_from_html_invalid_html_():
    html = "x"
    result = aptoide_resource.extract_AptoidApp_from_html(html, aptoide_model.SCRAPING_PATTERNS)
    assert type(result) == str

def test_extract_ApptoidApp_from_html_valid_html():
    url = "https://livetopia-party.en.aptoide.com/app"
    html = scraping_utils.get_html_page(url)
    result = aptoide_resource.extract_AptoidApp_from_html(html, aptoide_model.SCRAPING_PATTERNS)
    assert type(result) == aptoide_model.AptoideApp