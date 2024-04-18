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
import json

user_dao = UserDao()
casino_dao = CasinoDao()
gametable_dao = GameTableDao()
bar_dao = BarDao()

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
    staffid_list = [row['id'] for row in stafflist]
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
    casinoA_list = []
    casinoB_list = []
    casinoC_list = []
    casinoD_list = []

    for casino_id in casino_list_json:
        if casino_id['id'].startswith('casinoA_'):
            casinoA_list.append(casino_id['id'])
        elif casino_id['id'].startswith('casinoB_'):
            casinoB_list.append(casino_id['id'])
        elif casino_id['id'].startswith('casinoC_'):
            casinoC_list.append(casino_id['id'])
        elif casino_id['id'].startswith('casinoD_'):
            casinoD_list.append(casino_id['id'])
    final_list = [casinoA_list, casinoB_list, casinoC_list, casinoD_list]
    # print(final_list)
    return jsonify({'status': 'Success', "casino_list": final_list})

def get_casino_tables(casinoId):
    table_list_casino = casino_dao.get_table_casinos(casinoId)
    table_list_json = [dict(row) for row in table_list_casino]
    tableA_list = []
    tableB_list = []
    tableC_list = []
    tableD_list = []

    for table_id in table_list_json:
        if table_id['gametableid'].startswith('gametableA_'):
            tableA_list.append(table_id['gametableid'])
        elif table_id['gametableid'].startswith('gametableB_'):
            tableB_list.append(table_id['gametableid'])
        elif table_id['gametableid'].startswith('gametableC_'):
            tableC_list.append(table_id['gametableid'])
        elif table_id['gametableid'].startswith('gametableD_'):
            tableD_list.append(table_id['gametableid'])
    final_list = [tableA_list, tableB_list, tableC_list, tableD_list]
    # print("final_list: ", final_list)
    return jsonify({'status': 'Success', "table_list": final_list})

def get_casino_bars(casinoId):
    bar_list_casino = casino_dao.get_bar_casinos(casinoId)
    bar_list_json = [dict(row) for row in bar_list_casino]
    bar_list = []
    for bar_id in bar_list_json:
        if bar_id['barid'].startswith('bar_'):
            bar_list.append(bar_id['barid'])
    return jsonify({'status': 'Success', "bar_list": bar_list})

def get_casino_tokencounterid(casinoId):
    tokencounterid = casino_dao.get_tokencounter_casinos(casinoId)
    tokencounter_list_json = [dict(row) for row in tokencounterid]
    # print("tokencounterid: ", tokencounterid)
    return jsonify({'status': 'Success', "tokencounterid": tokencounter_list_json})

@app.route('/casino_info',methods=['POST'])
def get_casino_info():
    print("Getting casino info")
    casinoId = request.json['casinoId']
    casino_info = {}
    casino_info['table_list'] = get_casino_tables(casinoId).json['table_list']
    casino_info['bar_list'] = get_casino_bars(casinoId).json['bar_list']
    casino_info['tokencounterid'] = get_casino_tokencounterid(casinoId).json['tokencounterid'][0]['tokencounterid']
    return jsonify({'status': 'Success', 'casino_info': casino_info})

@app.route('/gametable_info',methods=['POST'])
def get_gametable_info():
    print("Getting gametable info")
    gametableId = request.json['gametableId']
    gametable_info = gametable_dao.get_table_info(gametableId)
    gametable_dict = dict(gametable_info)

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
    staffid_list = [row['id'] for row in stafflist]

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
    gametable_dao.update_gametable_staff(gametableId, staffId)
    return jsonify({'status': 'Success'})

@app.route('/update_bar_staff',methods=['POST'])
def update_bar_staff():
    print("Updating bar staff")
    barId = request.json['barId']
    staffId = request.json['staffId']
    bar_dao.update_bar_staff(barId, staffId)
    return jsonify({'status': 'Success'})