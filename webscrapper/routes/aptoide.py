import falcon  # type: ignore
from typing import Type
from webscrapper.resources.aptoide import AptoideAppResource

# Aptoide Website Scraping routes
def add_aptoide_routes(app: Type[falcon.App]) -> None:
    aptoide_app: AptoideAppResource = AptoideAppResource()
    app.add_route('/aptoideapp/', aptoide_app)