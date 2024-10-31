from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import cấu hình
    from app.configs.config import Config
    app.config.from_object(Config)

    # Khởi tạo database
    from app.main.database import db
    db.init_app(app)

    # Khởi tạo các routes, blueprints, v.v.
    from app.main.api import api
    api.init_app(app)

    return app

