from flask import jsonify
from app import app
from app.dao.UserDao import UserDao
from app.dao.ManagerDao import ManagerDao
from flask import request

from app.dao.ManagerDao import ManagerDao
from flask import request


user_dao = UserDao()
manager_dao = ManagerDao()
manager_dao = ManagerDao()
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_dao.get_user_by_id(user_id)
    if user:
        return jsonify(user.serialize())
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/add', methods=['POST'])
def add_user():
    # print("i am here")
    username = request.json['username']
    email = request.json['email']
    age = request.json['age']
    password = request.json['password']
    user_id = user_dao.create_user(username, email, age, password)
    user_dao.create_user_token_wallet(user_id)
    return jsonify({'id': user_id})

@app.route('/subscribe', methods=['POST'])
def subscribe():
    print("here")
    userId = request.json['userId']
    casinoId = request.json['casinoId']
    if(user_dao.check_user_subscription(userId, casinoId) == False):
        user_dao.create_user_subscription(userId, casinoId)
        return jsonify({'status': 'subscribed'})
    else:
        user_dao.remove_user_subscription(userId, casinoId)
        return jsonify({'status': 'unsubscribed'})

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

@app.route('/avail_staff', methods=['POST'])
def get_avail_staff():
    print("here")
    staff_data = user_dao.get_all_avail_staff()
    staff_id_list = [row["staffid"] for row in staff_data]
    staff_name_list = [row["name"] for row in staff_data]
    staff_data_json = {"staffid": staff_id_list, "staffname": staff_name_list}
    return {"avail_staff": staff_data_json}

@app.route('/add_staff', methods=['POST'])
def add_staff():
    name = request.json['Name']
    salary = request.json['Salary']
    staff_id = user_dao.add_staff(name, salary)
    print(staff_id)
    return jsonify({'id': staff_id})

@app.route("/check_subscription", methods=['POST'])
def check_subscription():
    userId = request.json['userId']
    casinoId = request.json['casinoId']
    if(user_dao.check_user_subscription(userId, casinoId)):
        return jsonify({'status': 'subscribed'})
    else:
        return jsonify({'status': 'not_subscribed'})