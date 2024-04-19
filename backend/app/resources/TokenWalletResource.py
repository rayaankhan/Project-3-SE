from flask import jsonify
from app import app
from flask import request

from app.dao.TokenWalletDao import TokenWalletDao

@app.route('/wallet/balance', methods=['GET'])
def get_wallet_balance():
    wallet_id = request.args.get('wallet_id')
    token_wallet_dao = TokenWalletDao()
    balance = token_wallet_dao.get_wallet_balance(wallet_id)
    return jsonify(balance)

@app.route('/wallet/update', methods=['POST'])
def update_wallet_balance():
    wallet_id = request.json['wallet_id']
    amount = request.json['amount']
    token_wallet_dao = TokenWalletDao()
    wallet_id = token_wallet_dao.update_wallet_balance(wallet_id, amount)
    return jsonify(wallet_id)

@app.route('/wallet/addBalance', methods=['POST'])
def add_balance():
    wallet_id = request.json['wallet_id']
    amount = request.json['amount']
    earlier_balance = get_wallet_balance(wallet_id)
    update_wallet_balance(wallet_id, earlier_balance + amount)
    return jsonify({"status": "success"})