from flask import jsonify
from app import bcrypt
from app import app
from app.dao.ManagerDao import ManagerDao
from flask import request

manager_dao = ManagerDao()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

@app.route('/manager/add', methods=['POST'])
def add_manager():
    username = request.json['username']
    email = request.json['email']
    age = request.json['age']
    password = request.json['password']
    salary = request.json['salary']
    password = hash_password(password)
    manager_id = manager_dao.create_manager(username, email, age, password, salary)
    return jsonify({'id': manager_id})
