from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.api.routes import users


def set_routers(app: FastAPI):
    app.include_router(users.router)


def set_database(app: FastAPI):
    # Make the settings to connect to database
    # the sqlite3 database is temporary
    register_tortoise(
            app=app,
            config={
                'connections': {
                    'default': 'sqlite://db.sqlite3'
                },
                'apps': {
                    'models': {
                        'models': [
                            'src.datalayer.models.user'
                        ],
                        'default_connection': 'default',
                    }
                }
            },
            generate_schemas=True,
            add_exception_handlers=True
    )
