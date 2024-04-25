from flask import jsonify
from app import app
from flask import request

from app.dao.TokenWalletDao import TokenWalletDao

@app.route('/wallet/balance', methods=['GET'])
def get_wallet_balance():
    user_id = request.args.get('user_id')
    print("user_id",user_id)
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
    strategy = request.json['strategy'] 
    currency = request.json['currency']
    token_wallet_dao = TokenWalletDao()
    earlier_balance = token_wallet_dao.get_wallet_balance(user_id)
    final_amt=process_payment(user_id, amount, strategy,currency)
    
    total = earlier_balance + int(final_amt)
    
    token_wallet_dao.update_wallet_balance(user_id, total)
    return jsonify({"status": "success"})

@app.route('/wallet/addRecordBalance', methods=['POST'])
def add_record_balance():
    user_id = request.json['user_id']
    amount = request.json['amount']
    strategy = request.json['strategy'] 
    currency = request.json['currency']
    casino_id = request.json['casino_id']
    token_wallet_dao = TokenWalletDao()
    earlier_balance = token_wallet_dao.get_wallet_balance(user_id)
    final_amt=process_payment(user_id, amount, strategy,currency)
    if int(amount)<0:
        token_wallet_dao.update_transaction(user_id, casino_id, final_amt, "debit")
    else:
        token_wallet_dao.update_transaction(user_id, casino_id, final_amt, "credit")
    
    total = earlier_balance + int(final_amt)
    
    token_wallet_dao.update_wallet_balance(user_id, total)
    return jsonify({"status": "success"})

@app.route('/bar/pay', methods=['POST'])
def pay_bar():
    user_id = request.json['user_id']
    amount = request.json['amount']
    strategy = request.json['strategy'] 
    token_wallet_dao = TokenWalletDao()
    # earlier_balance = token_wallet_dao.get_wallet_balance(user_id)
    # total = earlier_balance + int(amount)
    process_payment(user_id, amount, strategy)
    # token_wallet_dao.update_wallet_balance(user_id, total)
    return jsonify({"status": "success"})