from flask import jsonify
from app import app
from flask import request

from app.dao.TokenWalletDao import TokenWalletDao
from app.models.builder.ConcreteStrategy import CashPayment,CardPayment,UpiPayment
from app.models.builder.USDAdapter import CurrencyConverter,PaymentStrategyAdapter
# Function to handle payment
def process_payment(user_id, amount, payment_method,currency="INR"):
    # Select payment strategy based on the chosen method
    if payment_method == 'cash':
        payment_context = CashPayment()
        if currency == "USD":
            currency_converter = CurrencyConverter()
            payment_context = PaymentStrategyAdapter(payment_context, currency_converter)   
    elif payment_method == 'card':
        payment_context = CardPayment()
    elif payment_method == 'upi':
        payment_context = UpiPayment()
    else:
        return {"status": "error", "message": "Invalid payment method"}

    # Make payment using the selected strategy
    payment_context.authorize()
    final_amt=payment_context.pay(amount)
    return final_amt

@app.route('/wallet/balance', methods=['GET'])
def get_wallet_balance():
    user_id = request.args.get('user_id')
    token_wallet_dao = TokenWalletDao()
    balance = token_wallet_dao.get_wallet_balance(user_id)
    return jsonify(balance)

@app.route('/wallet/create', methods=['POST'])
def create_wallet():
    user_id = request.json['user_id']
    token_wallet_dao = TokenWalletDao()
    user_id = token_wallet_dao.create_wallet(user_id)
    return jsonify(user_id)

@app.route('/wallet/update', methods=['POST'])
def update_wallet_balance():
    user_id = request.json['user_id']
    amount = request.json['amount']
    token_wallet_dao = TokenWalletDao()
    user_id = token_wallet_dao.update_wallet_balance(user_id, amount)
    return jsonify(user_id)

@app.route('/wallet/addBalance', methods=['POST'])
def add_balance():
    user_id = request.json['user_id']
    amount = request.json['amount']
    strategy = request.json['strategy'] 
    currency = request.json['currency']
    token_wallet_dao = TokenWalletDao()
    earlier_balance = token_wallet_dao.get_wallet_balance(user_id)
    final_amt=process_payment(user_id, amount, strategy,currency)
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