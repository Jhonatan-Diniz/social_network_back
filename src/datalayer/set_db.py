from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def set_database(app: FastAPI):
    # Make the settings to connect to database
    # the sqlite3 database is temporary
    configs = {
        'connections': {'default': 'sqlite://db.sqlite3'},
        'apps': {
            'models': {
                'models': ['src.datalayer.models.user'],
            }
        }
    }

    # Init the Tortoise connection with the sqlite3 database
    # and setup the configs
    register_tortoise(
            app=app,
            config=configs,
    )
