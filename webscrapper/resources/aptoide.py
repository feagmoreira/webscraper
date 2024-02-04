import json
import falcon
import re
from codecs import unicode_escape_decode
from typing import Type, BinaryIO
from urllib.error import URLError
from urllib.request import urlopen
from urllib.parse import urlparse
from webscrapper.model.aptoide import AptoideApp, SCRAPING_PATTERNS

def get_html_page(url: str) -> str:
    
    # Http call to get html code from remote page
    try:
         page: BinaryIO  = urlopen(url)

    # Error handling for urlopen call
    except URLError as e:
        reason: str = e.reason
        return "Error getting html: " + reason
    
    # Error handling for invalir URL - URL ValueError
    except ValueError as e:
        return "Error getting html: "+ str(e)

    # Extracting html content as raw string
    html_content_raw: str = page.read().decode("utf-8")

    return html_content_raw

def extract_AptoidApp_from_html(html: str, patterns: dict[str,str]) -> Type[AptoideApp] | str: 
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
            attributes[key]  = unicode_escape_decode(result_raw)[0]
        else:
            return "Error scraping html: No match found for attribute " + key
         
    extracted_app: Type[AptoideApp] = AptoideApp(attributes["name"], attributes["version"], attributes["downloads"], attributes["release_date"], attributes["description"])
    
    return extracted_app

def validate_url(url: str)-> bool:
    # Use urlparse function to validate url format and components
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

class AptoideAppResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
       url: str = req.params["url"]
       print(url)
       # Validate user input (URL)
       url_valid: bool = validate_url(url)
       
       if url_valid:
            # Get html from Aptoide website
            html: str = get_html_page(url)

            # Validate Return from get_html_page function
            if "Error getting html" not in html:
                # Scraping html and returning object
                app_obj: Type[AptoideApp] | str = extract_AptoidApp_from_html(html, SCRAPING_PATTERNS)

                # Validating scraping response and returning response object to client
                if type(app_obj) != str:
                    resp.text = json.dumps(app_obj.__dict__)
                    resp.status = falcon.HTTP_200
                else:
                    resp.text = app_obj
                    resp.status = falcon.HTTP_500
            else:
                resp.text = html
                resp.status = falcon.HTTP_500
       else:
           resp.text = "Error: Invalid url format input"
           resp.status = falcon.HTTP_400



  


    

