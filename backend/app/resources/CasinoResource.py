from flask import jsonify
from app import app
# from app.dao.CasinoDao import CasinoDao
from flask import request
from app.models.builder.CasinoDirector import CasinoDirector
from app.models.builder.CasinoBuilder import CasinoBuilder
from app.models.builder.ConcreteCasinoBuilder import ConcreteCasinoBuilder

# user_dao = CasinoDao()

@app.route('/casino/add',methods=['POST'])
def add_casino():
    casinoType = request.json['casinoType']
    tableA = request.json(['tableA'])
    tableB = request.json(['tableB'])
    tableC = request.json(['tableC'])
    tableD = request.json(['tableD'])
    num_bar = request.json(['num_bar'])
    stafflist = []
    director = CasinoDirector()
    builder = ConcreteCasinoBuilder()
    if(casinoType==1):
        director.constructCasinoA(builder,tableA,tableC,num_bar,stafflist)
    elif(casinoType==2):
        director.constructCasinoB(builder,tableA,tableB,num_bar,stafflist)
    elif(casinoType==3):
        director.constructCasinoC(builder,tableC,tableD,num_bar,stafflist)
    else:
        director.constructCasinoD(builder,tableB,tableD,num_bar,stafflist)

    casinoId = builder.getResult()

# @app.route('/users/add', methods=['POST'])
# def add_user():
#     username = request.json['username']
#     email = request.json['email']
#     age = request.json['age']
#     password = request.json['password']
#     user_id = user_dao.create_user(username, email, age, password)
#     return jsonify({'id': user_id})

# @app.route('/users/login', methods=['POST'])
# def login():
#     username = request.json['username']
#     password = request.json['password']
#     user = user_dao.get_user_by_username(username)
#     if user and user.get_password() == password:
#         return jsonify(user.serialize())
#     return jsonify({'error': 'Invalid credentials'}), 401
