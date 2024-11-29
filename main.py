from fastapi import FastAPI
from src.datalayer.set_db import set_database


def createApp() -> FastAPI:
    # returns the app Object

    # Initilize the FastAPI Object appication
    app = FastAPI()

    # Initilize and setup the database configs
    set_database(app)

    return app


app = createApp()
