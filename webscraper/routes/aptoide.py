"""
Contains endpoint routes related to Aptoide website

Functions
---------
add_aptoide_routes - configures routes in a Falcon Web Framework (https://falcon.readthedocs.io/en/stable/) App object

"""
import falcon  # type: ignore
from typing import Type
from webscraper.resources.aptoide import AptoideAppResource

# Aptoide Website Scraping endpoint routes
def add_aptoide_routes(app: Type[falcon.App]) -> None:
    """
        Includes Aptoide website endpoint routes to a Falcon Web Framework (https://falcon.readthedocs.io/en/stable/) App object.
        Links endpoint path with falcon resource class that will treat requests

        Parameters
        ----------
        app : falcon.App
            Falcon Web Framework App object that will be hosted by the webserver

    """
    aptoide_app: AptoideAppResource = AptoideAppResource()
    app.add_route('/aptoideapp/', aptoide_app)