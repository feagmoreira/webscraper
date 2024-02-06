"""
Contains the Falcon Web Framework (https://falcon.readthedocs.io/en/stable/) APP the main entry point of webscraperapp using Falcon-based
WSGI app that will be hosted in the web server.

"""
import falcon # type: ignore
from webscrapper.routes.aptoide import add_aptoide_routes

app = application = falcon.App(cors_enable=True)

# Adding aptoide routes
add_aptoide_routes(app)

