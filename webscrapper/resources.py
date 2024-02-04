import json
import falcon
import urllib
import re
from typing import Type, BinaryIO
from urllib.request import urlopen
from model import AptoideApp

def get_html_page(url: str) -> str:
    
    # Http call to get html code from remote page
    try:
         page: BinaryIO  = urlopen(url)

    # Error handling for urlopen call
    except urllib.error.URLError as e:
        reason: str = e.reason
        return "Error: " + reason
    
    # Error handling for invalir URL - URL ValueError
    except ValueError as e:
        return str(e)

    # Extracting html content as string
    html_content: str = page.read().decode("utf-8")

    return html_content

def extract_text_from_html(html: str, start_pattern: str, end_pattern: str ) -> str:
    

    

