from flask import jsonify
from app import app
from app.dao.UserDao import UserDao
from app.dao.ManagerDao import ManagerDao
from flask import request


user_dao = UserDao()
manager_dao = ManagerDao()
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_dao.get_user_by_id(user_id)
    if user:
        return jsonify(user.serialize())
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/add', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    age = request.json['age']
    password = request.json['password']
    user_id = user_dao.create_user(username, email, age, password)
    return jsonify({'id': user_id})

@app.route('/users/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = user_dao.get_user_by_username(username)
    response = None
    if user and user.get_password() == password:
        manager = manager_dao.get_manager_by_id(user.get_id())
        response = user.serialize()
        if(user.get_username() == 'admin'):
            # add a variable role to the user object
            response['role'] = 'admin'
            response = jsonify(response)
        elif manager:
            # add a variable role to the user object
            response['role'] = 'manager'
            response = jsonify(response)
        else:
            # add a variable role to the user object
            response['role'] = 'user'
            response = jsonify(response)
    else:
        response = jsonify({'error': 'Invalid credentials'}), 401
    return response
