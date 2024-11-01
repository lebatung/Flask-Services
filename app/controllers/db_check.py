from flask import jsonify
from flask_restful import Resource
from sqlalchemy import text
from app.main.database import db

class CheckDatabase(Resource):
    def get(self):
        try:
            # Sử dụng `.mappings()` để nhận kết quả dưới dạng dictionary
            result = db.session.execute(text("SELECT TOP 1 * FROM dbo.Users")).mappings().fetchone()
            # Trả về dữ liệu trực tiếp nếu `result` không rỗng
            data = dict(result) if result else None
            return jsonify({"status": "success", "data": data})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)})
