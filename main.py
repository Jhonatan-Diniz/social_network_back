from fastapi import FastAPI
from src.settings import set_database, set_routers


def createApp() -> FastAPI:
    # returns the app Object

    # Initilize the FastAPI Object appication
    app = FastAPI()

    # Initilize and setup the database configs
    set_database(app)

    # Setup the routers paths
    set_routers(app)

    return app


app = createApp()
