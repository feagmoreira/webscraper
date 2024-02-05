import json
import falcon
import re
from codecs import unicode_escape_decode
from typing import Type
from webscrapper.utils.scraping_utils import validate_url, get_html_page
from webscrapper.model.aptoide import AptoideApp, SCRAPING_PATTERNS

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
            return "Error scraping html. No match found for attribute: " + key
         
    extracted_app: Type[AptoideApp] = AptoideApp(attributes["name"], attributes["version"], attributes["downloads"], attributes["release_date"], attributes["description"])
    
    return extracted_app

class AptoideAppResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
       url: str = req.params["url"]
       
       # Validate user input (URL)
       url_valid: bool = validate_url(url)
       
       if url_valid:
            # Get html from Aptoide website
            html: str = get_html_page(url)

            # Validate Return from get_html_page function
            if "Error getting html" not in html:
                #Inlusing console log message in the server
                print("Scraping url: " + url)
                # Scraping html and returning object
                app_obj: Type[AptoideApp] | str = extract_AptoidApp_from_html(html, SCRAPING_PATTERNS)

                # Validating scraping response and returning response object to client
                if type(app_obj) != str:
                    resp.text = json.dumps(app_obj.__dict__)
                    resp.status = falcon.HTTP_200
                else:
                    error: dict[str,str] = {"error": app_obj}
                    resp.text = json.dumps(error)
                    resp.status = falcon.HTTP_500
            else:
                error: dict[str,str] = {"error": html}
                resp.text = json.dumps(error)
                resp.status = falcon.HTTP_500
       else:
           error: dict[str,str] = {"error":"Invalid url format input"}
           resp.text = json.dumps(error)
           resp.status = falcon.HTTP_400



  


    

