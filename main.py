from fastapi import FastAPI
from src.settings import set_database, set_routers
from fastapi.middleware.cors import CORSMiddleware


def createApp() -> FastAPI:
    # Initilize the FastAPI Object appication
    app = FastAPI()

    # returns the app Object
    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:7000",
        "http://localhost:8000",
        ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Initilize and setup the database configs
    set_database(app)

    # Setup the routers paths
    set_routers(app)

    return app


app = createApp()
