#Scraping Utility Functions
from typing import BinaryIO
from urllib.error import URLError
from urllib.request import urlopen
from urllib.parse import urlparse

def validate_url(url: str)-> bool:
    # Use urlparse function to validate url format and components
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    
def get_html_page(url: str) -> str:
    
    # Http call to get html code from remote page
    try:
         page: BinaryIO  = urlopen(url)

    # Error handling for urlopen call
    except URLError as e:
        reason: str | BaseException = e.reason
        if type(reason) == str:
            return "Error getting html: " + reason
        else:
            return "Error getting html: Internal error"
    
    # Error handling for invalir URL - URL ValueError
    except ValueError as e:
        return "Error getting html: "+ str(e)

    # Extracting html content as raw string
    html_content_raw: str = page.read().decode("utf-8")

    return html_content_raw