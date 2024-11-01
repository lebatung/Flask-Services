# app/controllers/user.py
from flask_restful import Resource

class UserList(Resource):
    def get(self):
        # Logic để lấy danh sách người dùng
        return {'users': []}  # Thay thế bằng danh sách thực tế

    def post(self):
        # Logic để tạo người dùng mới
        return {'message': 'User created'}, 201


class User(Resource):
    def get(self, id):
        # Logic để lấy thông tin người dùng theo ID
        return {'user': {'id': id}}  # Thay thế bằng thông tin thực tế

    def put(self, id):
        # Logic để cập nhật người dùng theo ID
        return {'message': f'User {id} updated'}, 200

    def delete(self, id):
        # Logic để xóa người dùng theo ID
        return {'message': f'User {id} deleted'}, 204
