"""
Contains general utility functions used to support web scraping tools.

Functions
---------
validate_url - validate input urls that will be scraped \n
get_html_page - grabs the page html and returns as a raw string that will be used for scraping

"""
#Scraping Utility Functions
from typing import BinaryIO
from urllib.error import URLError
from urllib.request import urlopen
from urllib.parse import urlparse

def validate_url(url: str)-> bool:
    """
      Validates a given url string to check if it has all the componentes to match format RFC on Relative Uniform Resource Locators (addressing scheme, network location, path)
      
      Uses the urlparse function from urllib.parse library (https://docs.python.org/3/library/urllib.parse.html) that extracts information of a given
      
      string and returns a an absolute URL. If urlparse function can build the URL, validate_url will return true and if it fails ir will return false.

        Parameters
        ----------
        url : str
            The url string to be evaluated
    
    """
    # Use urlparse function to validate url format and components
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    
def get_html_page(url: str) -> str:
    """
      Used to grab the html code of a given url and return it as raw string to be scraped by a scraping tool.

      Uses the urlopen function from urllib.request library (https://docs.python.org/3/library/urllib.request.html) to make the http get call to retrive html code from page as bytes
      that are later coverted into raw string.

      If the html code cannot be obtained, errors are returned to the user as strings with a message and reason code.
      
        Parameters
        ----------
        url : str
            The url string 
    
    """
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
    
    # Error handling for invalid URL - URL ValueError
    except ValueError as e:
        return "Error getting html: "+ str(e)

    # Extracting html content as raw string
    html_content_raw: str = page.read().decode("utf-8")

    return html_content_raw