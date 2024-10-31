import os
from flask import Flask
from app import main
from app.main.database import db, migration
from app.configs.config import Config  # Nhập Config từ config
# Flask App Initialization
app = Flask(__name__)
app.config.from_object(Config)  # Cần chắc chắn rằng bạn nhập đúng class Config từ config

# Database ORM Initialization
db.init_app(app)

# Database Migrations Initialization
migration.init_app(app, db)

# Khởi động ứng dụng
if __name__ == '__main__':
    app.run(debug=True)
