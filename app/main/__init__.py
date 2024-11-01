from flask import Flask
from app.configs.config import Config
from app.main.database import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)  #

    from app.main.api import api
    api.init_app(app)

    return app
