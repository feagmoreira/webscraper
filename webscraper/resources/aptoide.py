"""
Contains API endpoint class for scraping app information from Aptoide website

Classes
---------
AptoideAppResource - falcon Resource class that implements GET request handler method

Functions
---------
extract_AptoidApp_from_html - extracts information from html raw text and returns AptoideApp object

"""
import json
import falcon # type: ignore
import re
from codecs import unicode_escape_decode
from webscraper.utils.scraping_utils import validate_url, get_html_page
from webscraper.model.aptoide import AptoideApp, SCRAPING_PATTERNS

def extract_AptoidApp_from_html(html: str, patterns: dict[str,str]) -> AptoideApp | str: 
    """
    Function extract information from a raw html string previously retrieved from a webpage, based on a patterns dictionary.

    Retrieved data is used to build and return an AptoideApp object.

    If required information specified in the patterns dictionary cannot be found, returns an error message with the name of the attribute that could not be found in the html string  

        Parameters
        ----------
        htlm : str
            raw html string previously extracted from a website for scrapping
        patterns: dict[str,str]
            dictionary containing attribute names and patterns that will be used for the search of the required data in the html
    
    """
     # Removing empty HTML comments
    html = re.sub("<!-- -->","", html)

    attributes: dict[str,str] = {}
    for key in patterns:
        # Searching for desired substring
        result_match: re.Match[str] | None = re.search(patterns[key], html)
        
        # Check if result is valid 
        if result_match:     
            # Extracting desired substring
            result_raw: str = result_match.group(1)

            #Replacing unicode characters with backslash representation (necessary to avoid wrong conversion from decoding)
            result_raw_bytes: bytes = result_raw.encode('ascii','backslashreplace')

            # Converting from raw string to regular string to use website original formatting 
            attributes[key]  = unicode_escape_decode(result_raw_bytes)[0]
        else:
            return "Error scraping html. No match found for attribute: " + key
         
    # Creating AptoideApp object from extracted attributes
    extracted_app: AptoideApp = AptoideApp(attributes["name"], attributes["version"], attributes["downloads"], attributes["release_date"], attributes["description"])
    
    return extracted_app

class AptoideAppResource:
    """
    Falcon Web Framework (https://falcon.readthedocs.io/en/stable/) Resource class that implements GET request handler for the endpoint /aptoideapp/

    Methods
    -------
    on_get - GET request handler for enpoint /aptoideapp/

    """
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
       """
        GET request handler for endpoint /aptoideapp/.

        Receives from the client url as a query parameter, validates and obtains html string from url using utils functions and extracts and returns as a response
        to the GET request the app information obtained from the extract_AptoidApp_from_html function.

        If any errors occur during any step of the process, an error message with details about the problem is returned to the client as a json object in the falcon response object with the corresponding Http status code:
        - Status 500 for errors during html extraction and scraping steps
        - Status 400 for invalid url format (user input)

        Parameters
        ----------
        req : falcon.Request
            Falcon Web Framework Request object that holds details about the http request sent to the endpoint by the client
        res: falcon.Response
            Falcon Web Framework Response object that is used to send the response of the processing executed by the get handler
    
    """
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
                app_obj: AptoideApp | str = extract_AptoidApp_from_html(html, SCRAPING_PATTERNS)

                # Validating scraping response and returning response object to client
                if type(app_obj) != str:
                    resp.text = json.dumps(app_obj.__dict__)
                    resp.status = falcon.HTTP_200
                # Error obtaining apps information from html text
                else:
                    scraping_error: dict[str,str] = {"error": app_obj}
                    resp.text = json.dumps(scraping_error)
                    resp.status = falcon.HTTP_500
            # Error getting html string from valid url
            else:
                html_error: dict[str,str] = {"error": html}
                resp.text = json.dumps(html_error)
                resp.status = falcon.HTTP_500
       # Error form url validation
       else:
           url_error: dict[str,str] = {"error":"Invalid url format input"}
           resp.text = json.dumps(url_error)
           resp.status = falcon.HTTP_400



  


    

