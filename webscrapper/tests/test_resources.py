import pytest

import webscrapper.resources.aptoide as aptoide_resource
import webscrapper.model.aptoide as aptoide_model
import webscrapper.utils.scraping_utils as scraping_utils

def test_extract_ApptoidApp_from_html_invalid_html_():
    html = "x"
    result = aptoide_resource.extract_AptoidApp_from_html(html, aptoide_model.SCRAPING_PATTERNS)
    assert type(result) == str

def test_extract_ApptoidApp_from_html_valid_html():
    url = "https://livetopia-party.en.aptoide.com/app"
    html = scraping_utils.get_html_page(url)
    result = aptoide_resource.extract_AptoidApp_from_html(html, aptoide_model.SCRAPING_PATTERNS)
    assert type(result) == aptoide_model.AptoideApp