# app/controllers/user.py
from flask_restful import Resource

class UserList(Resource):
    def get(self):
        return {'users': []}

    def post(self):
        return {'message': 'User created'}, 201


class User(Resource):
    def get(self, id):
        return {'user': {'id': id}}

    def put(self, id):
        return {'message': f'User {id} updated'}, 200

    def delete(self, id):
        return {'message': f'User {id} deleted'}, 204
