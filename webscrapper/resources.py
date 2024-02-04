import json
import falcon
import urllib
import re
import codecs
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

    # Extracting html content as raw string
    html_content_raw: str = page.read().decode("utf-8")

    return html_content_raw

def extract_AptoidApp_from_html(html: str, patterns: dict[str,str]) -> Type[AptoideApp]: 
     # Removing empty HTML comments
    html = re.sub("<!-- -->","", html)

    attributes: dict[str,str] = {}
    for key in patterns:
        # Searching for desired substring
        result_match: re.Match = re.search(patterns[key], html)
        
        # Check if result is valid 
        if result_match:     
            # Extracting desired substring
            result_raw: str = result_match.group(1)

            #Replacing unicode characters with backslash representation (necessary to avoid wrong conversion from decoding)
            result_raw = result_raw.encode('ascii','backslashreplace')

            # Converting from raw string to regular string to use website original formatting 
            attributes[key]  = codecs.unicode_escape_decode(result_raw)[0]
        else:
            return "Error: No match found for attribute " + key
         
    extracted_app: Type[AptoideApp] = AptoideApp(attributes["name"], attributes["version"], attributes["downloads"], attributes["release_date"], attributes["description"])
    
    return extracted_app



    

