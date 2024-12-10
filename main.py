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
        "http://localhost:8000",
        "http://127.0.0.1:8000"
        'http://127.0.0.1:7000'
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Initilize and setup the database configs
    set_database(app)

    # Setup the routers paths
    set_routers(app)

    return app


app = createApp()
