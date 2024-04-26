from flask import jsonify, request
from app import app, bcrypt
from app.dao.UserDao import UserDao
from app.dao.ManagerDao import ManagerDao
from app.dao.SubscriptionDao import SubscriptionDao
from app.dao.CasinoDao import CasinoDao
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


user_dao = UserDao()
manager_dao = ManagerDao()
casino_dao = CasinoDao()

# Hash password before storing
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Verify password
def verify_password(plain_password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, plain_password)
class UserResource:
    @app.route('/users/<int:user_id>', methods=['GET'])
    @jwt_required()
    def get_user(user_id):
        user_id = get_jwt_identity()
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
        # hash the password before storing
        password = hash_password(password)
        user_id = user_dao.create_user(username, email, age, password)
        if user_id is None:
            return jsonify({'error': 'Username already taken'}), 400
        user_dao.create_user_token_wallet(user_id)
        return jsonify({'id': user_id})

    @app.route('/subscribe', methods=['POST'])
    @jwt_required()
    def subscribe():
        print("here")
        userId = get_jwt_identity()
        casinoId = request.json['casinoId']
        
        casino = casino_dao.get_casino(casinoId)
        if( casino.check_subscription(userId)):
            casino.detach(userId)
            return jsonify({'status': 'unsubscribed'})
        else:
            casino.attach(userId)
            return jsonify({'status': 'subscribed'})
            
                
    @app.route('/users/login', methods=['POST'])
    def login():
        username = request.json['username']
        password = request.json['password']
        user = user_dao.get_user_by_username(username)
        response = None
        if user and user.get_username() == 'admin':
            response = user.serialize()
            response['role'] = 'admin'
            access_token = create_access_token(identity=user.get_id(),  additional_claims={'role': 'admin'})
            response['access_token'] = access_token
            response = jsonify(response)
            return response
        if user and verify_password(password, user.get_password()):
            manager = manager_dao.get_manager_by_id(user.get_id())
            response = user.serialize()
            if(user.get_username() == 'admin'):
                response['role'] = 'admin'
                access_token = create_access_token(identity=user.get_id(),  additional_claims={'role': 'admin'})
                # response = jsonify(response)
                # response.set_cookie('access_token', access_token)
            elif manager:
                response['role'] = 'manager'
                # add a variable role to the user object
                access_token = create_access_token(identity=user.get_id(),  additional_claims={'role': 'manager'})
                # response = jsonify(response)
                # response.set_cookie('access_token', access_token)
            else:
                response['role'] = 'user'
                # add a variable role to the user object
                access_token = create_access_token(identity=user.get_id(),  additional_claims={'role': 'user'})
                # response = jsonify(response)
                # response.set_cookie('access_token', access_token)
            response['access_token'] = access_token
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
    @jwt_required()
    def check_subscription():
        userId = get_jwt_identity()
        casinoId = request.json['casinoId']
        print(userId)
        print(casinoId)
        casino = casino_dao.get_casino(casinoId)
        if( casino.check_subscription(userId)):
            return jsonify({'status': 'subscribed'})
        else:
            return jsonify({'status': 'unsubscribed'})
        
    @app.route('/get_user_notifications', methods=['POST'])
    @jwt_required()
    def get_user_notifications():
        userId = get_jwt_identity()
        print(userId)
        notifications = user_dao.get_user_notifications(userId)
        print(notifications)
        # to return the notifications first we need to convert the list of tuples to a list of dictionaries
        notifications_list = []
        for notification in notifications:
            notification_dict = {
                "message": notification[0],
                "casinoname": notification[1]
            }
            notifications_list.append(notification_dict)
        return jsonify({"notifications": notifications_list})
        
