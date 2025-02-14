from models import User
from flask import request
from schemas import UserSchema
from your_database_module import db

user_schema = UserSchema()

class UserDetailResource:
    def get(self, id):
        user = User.query.get(id)
        if user:
            return user_schema.dump(user)
        return {'message': 'User not found'}, 404

    def put(self, id):
        user = User.query.get(id)
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return user_schema.dump(user)
        return {'message': 'User not found'}, 404

    def delete(self, id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return '', 204
        return {'message': 'User not found'}, 404