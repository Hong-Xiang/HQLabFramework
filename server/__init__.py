""" Entry of server with RESTful API """
from flask import Flask, jsonify, abort

server = Flask(__name__)

tests = [
    {
        'id': 0,
        'name': 'TEST0',
        'descreption':  'DESP for test0'
    }
]


@server.route('/hqlf/api/v0.1/tests', methods=['GET'])
def get_tests():
    return jsonify({'tests': tests})

@server.route('/hqlf/api/v0.1/tests/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return jsonify({'test': tests[task_id]})




