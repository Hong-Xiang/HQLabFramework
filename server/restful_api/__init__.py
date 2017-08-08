from flask import Flask
from flask_restful import Resource, Api

server_api = Flask(__name__)
api = Api(server_api)

class Hello(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Hello, '/')
