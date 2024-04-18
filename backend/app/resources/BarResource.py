from flask import jsonify
from app import app
from app.dao.BarDao import BarDao
from flask import request

bar_dao = BarDao()

@app.route('/bar')
def getter():
    return {'message': 'Hello, World!'}

@app.route('/bar/add', methods=['POST'])
def add_bar():
    name = request.json['name']
    location = request.json['location']
    manager = request.json['manager']
    bar_id = bar_dao.create_bar(name, location, manager)
    return jsonify({'id': bar_id})
