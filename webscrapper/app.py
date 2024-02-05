import falcon # type: ignore
from webscrapper.routes.aptoide import add_aptoide_routes

app = application = falcon.App(cors_enable=True)

# Adding aptoide routes
add_aptoide_routes(app)

