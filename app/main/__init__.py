from flask import Flask
from app.configs.config import Config
from app.main.database import db, migrate  # Đảm bảo import đúng `migrate`

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Khởi tạo database
    db.init_app(app)
    migrate.init_app(app, db)  #

    # Khởi tạo các routes
    from app.main.api import api
    api.init_app(app)

    return app
