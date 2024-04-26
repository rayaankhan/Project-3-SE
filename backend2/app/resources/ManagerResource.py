from flask import jsonify
from app import bcrypt
from app import app
from app.dao.ManagerDao import ManagerDao
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.dao.CasinoDao import CasinoDao

casino_dao = CasinoDao()
manager_dao = ManagerDao()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

class ManagerResource:
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

    @app.route('/manager/casinos',methods=['POST'])
    @jwt_required()
    def get_manager_casinos():
        # print("i am here boy")
        # print(request.json)
        managerId = get_jwt_identity()
        casino_list_mg = casino_dao.get_casino_list_mg(managerId)
        casino_list_json = [dict(row) for row in casino_list_mg]
        # print(casino_list_json)
        casinoA_list_id = []
        casinoB_list_id = []
        casinoC_list_id = []
        casinoD_list_id = []

        casinoA_list_name = []
        casinoB_list_name = []
        casinoC_list_name = []
        casinoD_list_name = []

        for casino_id in casino_list_json:
            if casino_id['casinoid'].startswith('casinoA_'):
                casinoA_list_id.append(casino_id['casinoid'])
                casinoA_list_name.append(casino_id['casinoname'])
            elif casino_id['casinoid'].startswith('casinoB_'):
                casinoB_list_id.append(casino_id['casinoid'])
                casinoB_list_name.append(casino_id['casinoname'])
            elif casino_id['casinoid'].startswith('casinoC_'):
                casinoC_list_id.append(casino_id['casinoid'])
                casinoC_list_name.append(casino_id['casinoname'])
            elif casino_id['casinoid'].startswith('casinoD_'):
                casinoD_list_id.append(casino_id['casinoid'])
                casinoD_list_name.append(casino_id['casinoname'])
        final_id_list = [casinoA_list_id, casinoB_list_id, casinoC_list_id, casinoD_list_id]
        final_name_list = [casinoA_list_name, casinoB_list_name, casinoC_list_name, casinoD_list_name]
        # print(final_list)
        return jsonify({'status': 'Success', "casino_id_list": final_id_list, "casino_name_list": final_name_list})
