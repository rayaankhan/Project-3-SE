from flask import jsonify
from app import bcrypt
from app import app
from app.dao.ManagerDao import ManagerDao
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.dao.CasinoDao import CasinoDao
from app.dao.GameTableDao import GameTableDao
from app.dao.UserDao import UserDao
from app.dao.StaffDao import StaffDao
from app.models.builder.GameTable import GameTable
from app.dao.BarDao import BarDao
import json

user_dao = UserDao()
casino_dao = CasinoDao()
manager_dao = ManagerDao()
gametable_dao = GameTableDao()
staff_dao = StaffDao()
bar_dao = BarDao()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')


class GameTableResource:
    @app.route('/play', methods=['POST'])
    def play():
        print("Playing game")
        gametableId = request.json['gametableId']
        user_amount = int(request.json['amount'])
        gametable_info = gametable_dao.get_table_info(gametableId)
        gametable_dict = dict(gametable_info)
        gametable = GameTable(gametable_dict['gametableid'], gametable_dict['name'], gametable_dict['staffid'], gametable_dict['prob'], gametable_dict['type'])
        final_amount = gametable.play(user_amount)
        casinoid = casino_dao.get_casino_id_by_gametableid(gametableId)
        # print(type(casinoid))
        # print(casinoid)
        gametable_dao.add_play_transaction(casinoid, gametableId, user_amount - final_amount)
        return jsonify({'status': 'Success', 'final_amount': final_amount})
    
    @app.route('/delete_gametable',methods=['POST'])
    def delete_gametable():
        print("Deleting gametable")
        gametableId = request.json['gametableId']
        print("gametableId: ", gametableId)
        gametable_info = gametable_dao.get_table_info(gametableId)
        staffid = gametable_info['staffid']
        print("staffid: ", staffid)
        staff_dao.update_staff_status(staffid, -1)
        gametable_dao.delete_gametable(gametableId)
        return jsonify({'status': 'Success'})
    
    @app.route('/update_gametable_staff',methods=['POST'])
    def update_gametable_staff():
        print("Updating gametable staff")
        gametableId = request.json['gametableId']
        staffId = request.json['staffId']
        oldStaffId = request.json['oldStaffId']
        print("oldStaffId: ", oldStaffId)
        staff_dao.update_staff_status(oldStaffId, -1)
        gametable_dao.update_gametable_staff(gametableId, staffId)
        staff_dao.update_staff_status(staffId, gametableId)
        return jsonify({'status': 'Success'})
    
    @app.route('/add_gametable_bar',methods=['POST'])
    def add_gametable_bar():
        print("Adding gametable and bar")
        casinoId = request.json['casinoId']
        tableA = int(request.json['A'])
        tableB = int(request.json['B'])
        tableC = int(request.json['C'])
        tableD = int(request.json['D'])
        bar = int(request.json['bar'])
        stafflist = user_dao.get_staff_list(tableA+tableB+tableC+tableD+bar)
        staffid_list = [row['staffid'] for row in stafflist]

        gameTableIdList = []
        barIdList = []

        i = 0

        for i in range(tableA):
            if(i >= len(staffid_list)):
                gameTableIdList.append(gametable_dao.create_gametableA("-1"))
            else:
                gameTableIdList.append(gametable_dao.create_gametableA(staffid_list[i]))
            i += 1
        for i in range(tableB):
            if(i >= len(staffid_list)):
                gameTableIdList.append(gametable_dao.create_gametableB("-1"))
            else:
                gameTableIdList.append(gametable_dao.create_gametableB(staffid_list[i]))
            i += 1
        for i in range(tableC):
            if(i >= len(staffid_list)):
                gameTableIdList.append(gametable_dao.create_gametableC("-1"))
            else:
                gameTableIdList.append(gametable_dao.create_gametableC(staffid_list[i]))
            i += 1
        for i in range(tableD):
            if(i >= len(staffid_list)):
                gameTableIdList.append(gametable_dao.create_gametableD("-1"))
            else:
                gameTableIdList.append(gametable_dao.create_gametableD(staffid_list[i]))
            i += 1
        for i in range(bar):
            if(i >= len(staffid_list)):
                barIdList.append(bar_dao.create_bar("-1", 5))
            else:
                barIdList.append(bar_dao.create_bar(staffid_list[i], 5))
            i += 1

        for gameTableId in gameTableIdList:
            casino_dao.add_gametable(gameTableId, casinoId)
        
        for barId in barIdList:
            casino_dao.add_bar(barId, casinoId)

        return jsonify({'status': 'Success'})
    
    @app.route('/gametable_info',methods=['POST'])
    def get_gametable_info():
        print("Getting gametable info")
        gametableId = request.json['gametableId']
        gametable_info = gametable_dao.get_table_info(gametableId)
        gametable_dict = dict(gametable_info)
        staff_assigned_name = staff_dao.get_staff_name(gametable_dict['staffid'])
        gametable_dict['staffname'] = staff_assigned_name
        # Now, convert the dictionary into JSON
        gametable_json = json.dumps(gametable_dict)
        return jsonify({'status': 'Success', 'gametable_info': gametable_json})
    
