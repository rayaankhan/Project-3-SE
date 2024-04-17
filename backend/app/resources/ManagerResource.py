from flask import jsonify
from app import app
from app.dao.ManagerDao import ManagerDao
from flask import request

manager_dao = ManagerDao()

@app.route('/manager/add', methods=['POST'])
def add_manager():
    username = request.json['username']
    email = request.json['email']
    age = request.json['age']
    password = request.json['password']
    salary = request.json['salary']
    manager_id = manager_dao.create_manager(username, email, age, password, salary)
    return jsonify({'id': manager_id})
