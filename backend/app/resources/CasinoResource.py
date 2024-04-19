from flask import jsonify
from app import app
# from app.dao.CasinoDao import CasinoDao
from flask import request
from app.models.builder.CasinoDirector import CasinoDirector
from app.models.builder.CasinoBuilder import CasinoBuilder
from app.models.builder.ConcreteCasinoBuilder import ConcreteCasinoBuilder
from app.dao.UserDao import UserDao
from app.dao.CasinoDao import CasinoDao
from app.dao.GameTableDao import GameTableDao
from app.dao.BarDao import BarDao
from app.dao.StaffDao import StaffDao
from app.models.builder.GameTable import GameTable
import json

user_dao = UserDao()
casino_dao = CasinoDao()
gametable_dao = GameTableDao()
bar_dao = BarDao()
staff_dao = StaffDao()

@app.route('/casino/add',methods=['POST'])
def add_casino():
    # print("i am here boy")
    print(request.json)
    managerId = request.json['userId']
    casinoType = request.json['casinoType']
    tableA = request.json['gameTableA']
    tableB = request.json['gameTableB']
    tableC = request.json['gameTableC']
    tableD = request.json['gameTableD']
    num_bar = request.json['bar']
    print("casinoType: ", casinoType)
    # print(tableA+tableB+tableC+tableD+num_bar)
    stafflist = user_dao.get_staff_list(tableA+tableB+tableC+tableD+num_bar)
    staffid_list = [row['staffid'] for row in stafflist]
    print("length of stafflist: ", len(staffid_list))
    builder: CasinoBuilder = ConcreteCasinoBuilder()
    director = CasinoDirector(builder, tableA, tableB, tableC, tableD, num_bar, staffid_list, casinoType)
    if(casinoType=='A'):
        director.constructCasinoA()
    elif(casinoType=='B'):
        director.constructCasinoB()
    elif(casinoType=='C'):
        director.constructCasinoC()
    elif(casinoType=='D'):
        director.constructCasinoD()
    else:
        print("Invalid casino")
        return jsonify({'id': -1})
    casinoId = builder.getResult(managerId, casinoType)
    if(casinoId == -1):
        return jsonify({'status': 'Failed'})
    return jsonify({'status': 'Success', 'id': casinoId})


@app.route('/manager_casinos',methods=['POST'])
def get_manager_casinos():
    # print("i am here boy")
    # print(request.json)
    managerId = request.json['managerId']
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

@app.route('/all_casinos',methods=['POST'])
def get_all_casinos():
    # print("i am here boy")
    # print(request.json)
    userId = request.json['userId']
    all_casino_list = casino_dao.get_all_casinos()
    casino_list_json = [dict(row) for row in all_casino_list]
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


def get_casino_tables(casinoId):
    table_list_casino = casino_dao.get_table_casinos(casinoId)
    table_list_json = [dict(row) for row in table_list_casino]
    tableA_id_list = []
    tableB_id_list = []
    tableC_id_list = []
    tableD_id_list = []

    tableA_name_list = []
    tableB_name_list = []
    tableC_name_list = []
    tableD_name_list = []

    for table_id in table_list_json:
        if table_id['gametableid'].startswith('gametableA_'):
            tableA_id_list.append(table_id['gametableid'])
            tableA_name_list.append(table_id['name'])
        elif table_id['gametableid'].startswith('gametableB_'):
            tableB_id_list.append(table_id['gametableid'])
            tableB_name_list.append(table_id['name'])
        elif table_id['gametableid'].startswith('gametableC_'):
            tableC_id_list.append(table_id['gametableid'])
            tableC_name_list.append(table_id['name'])
        elif table_id['gametableid'].startswith('gametableD_'):
            tableD_id_list.append(table_id['gametableid'])
            tableD_name_list.append(table_id['name'])
    final_id_list = [tableA_id_list, tableB_id_list, tableC_id_list, tableD_id_list]
    final_name_list = [tableA_name_list, tableB_name_list, tableC_name_list, tableD_name_list]

    # print("final_list: ", final_list)
    return jsonify({'status': 'Success', "table_id_list": final_id_list, "table_name_list": final_name_list})

def get_casino_bars(casinoId):
    bar_list_casino = casino_dao.get_bar_casinos(casinoId)
    bar_list_json = [dict(row) for row in bar_list_casino]
    bar_id_list = []
    bar_name_list = []
    for bar_id in bar_list_json:
        bar_id_list.append(bar_id['barid'])
        bar_name_list.append(bar_id['name'])
    return jsonify({'status': 'Success', "bar_id_list": bar_id_list, "bar_name_list": bar_name_list})

def get_casino_tokencounterid(casinoId):
    tokencounterid = casino_dao.get_tokencounter_casinos(casinoId)
    tokencounter_list_json = [dict(row) for row in tokencounterid]
    # print("tokencounterid: ", tokencounter_list_json)
    return jsonify({'status': 'Success', "tokencounterid": tokencounter_list_json})

@app.route('/casino_info',methods=['POST'])
def get_casino_info():
    print("Getting casino info")
    casinoId = request.json['casinoId']
    casino_info = {}

    table_info = get_casino_tables(casinoId)
    casino_info['table_id_list'] = table_info.json['table_id_list']
    casino_info['table_name_list'] = table_info.json['table_name_list']

    bar_info = get_casino_bars(casinoId)
    casino_info['bar_id_list'] = bar_info.json['bar_id_list']
    casino_info['bar_name_list'] = bar_info.json['bar_name_list']

    tokencounter_info = get_casino_tokencounterid(casinoId)
    casino_info['tokencounterid'] = tokencounter_info.json['tokencounterid'][0]['tokencounterid']
    return jsonify({'status': 'Success', 'casino_info': casino_info})

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
    # print("gametable_info: ", gametable_json)
    return jsonify({'status': 'Success', 'gametable_info': gametable_json})

@app.route('/bar_info',methods=['POST'])
def get_bar_info():
    print("Getting bar info")
    barId = request.json['barId']
    bar_info = bar_dao.get_bar_info(barId)
    bar_dict = dict(bar_info)
    # print("bar_dict: ", bar_dict['staffid'])
    staffname = staff_dao.get_staff_name(bar_dict['staffid'])
    print("staffname: ", staffname)
    bar_dict['staffname'] = staffname

    # Now, convert the dictionary into JSON
    bar_json = json.dumps(bar_dict)
    print("bar_info: ", bar_json)
    return jsonify({'status': 'Success', 'bar_info': bar_json})

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

@app.route('/update_bar_staff',methods=['POST'])
def update_bar_staff():
    print("Updating bar staff")
    barId = request.json['barId']
    staffId = request.json['staffId']
    oldStaffId = request.json['oldStaffId']
    print("oldStaffId: ", oldStaffId)
    staff_dao.update_staff_status(oldStaffId, -1)
    bar_dao.update_bar_staff(barId, staffId)
    staff_dao.update_staff_status(staffId, barId)
    return jsonify({'status': 'Success'})

@app.route('/delete_casino',methods=['POST'])
def delete_casino():
    print("Deleting casino")
    casinoId = request.json['casinoId']
    gametable_casino_list = casino_dao.get_table_casinos(casinoId)
    gametable_id = [row['gametableid'] for row in gametable_casino_list]
    bar_casino_list = casino_dao.get_bar_casinos(casinoId)
    bar_id = [row['barid'] for row in bar_casino_list]
    all_object_id = gametable_id + bar_id
    print("all_object_id: ", all_object_id)
    unassign_staff_all = casino_dao.unassign_staff(all_object_id)
    casino_dao.delete_casino_overall(casinoId)
    return jsonify({'status': 'Success'})

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

@app.route('/delete_bar', methods=['POST'])
def delete_bar():
    print("Deleting bar")
    barId = request.json['barId']
    bar_info = bar_dao.get_bar_info(barId)
    staffid = bar_info['staffid']
    print("staffId: ", staffid)
    staff_dao.update_staff_status(staffid, -1)
    bar_dao.delete_bar(barId)
    return jsonify({'status': 'Success'})

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

@app.route('/notify', methods=['POST'])
def notify():
    print("Notifying subsribers")
    casinoId = request.json['casinoId']
    managerId = request.json['managerId']
    text = request.json['text']
    
    subscriber_list_sql = user_dao.get_subscribers(casinoId)
    subscriber_list = [row['userid'] for row in subscriber_list_sql]
    print("subscriber_list: ", subscriber_list)
    
    # Yatharth has to implement here

    return jsonify({'status': 'Success'})