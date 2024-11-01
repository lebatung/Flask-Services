# app/__init__.py
import os
from flask import Flask
from app.main.database import db, migrate
from app.main.api import api  # Nhập API từ api.py
from app.configs.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Database Initialization
db.init_app(app)

# Migrations Initialization
migrate.init_app(app, db)

# API Initialization
api.init_app(app)

# Khởi động ứng dụng
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
