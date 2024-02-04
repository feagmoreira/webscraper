import falcon
from webscrapper.routes.aptoide import add_aptoide_routes

app = application = falcon.App()

# Adding aptoide routes
add_aptoide_routes(app)

