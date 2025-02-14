from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from resources.user_detail_resource import UserDetailResource
from resources.user_resource import UserResource
from config import Config

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(self.app)
        self.api = Api(self.app)

        # Add resources
        self.api.add_resource(UserResource, '/users')
        self.api.add_resource(UserDetailResource, '/users/<int:id>')

    def run(self):
        self.app.run(debug=True)