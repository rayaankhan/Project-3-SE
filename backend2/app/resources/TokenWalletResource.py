from flask import jsonify
from app import app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
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


class TokenWalletResource:
    @app.route('/wallet/balance', methods=['POST'])
    @jwt_required()
    def get_wallet_balance():
        user_id = get_jwt_identity()
        print("user_id",user_id)
        token_wallet_dao = TokenWalletDao()
        balance = token_wallet_dao.get_wallet_balance(user_id)
        return jsonify(balance)

    @app.route('/wallet/create', methods=['POST'])
    @jwt_required()
    def create_wallet():
        user_id = get_jwt_identity()
        token_wallet_dao = TokenWalletDao()
        user_id = token_wallet_dao.create_wallet(user_id)
        return jsonify(user_id)

    @app.route('/wallet/update', methods=['POST'])
    @jwt_required()
    def update_wallet_balance():
        user_id = get_jwt_identity()
        amount = request.json['amount']
        token_wallet_dao = TokenWalletDao()
        user_id = token_wallet_dao.update_wallet_balance(user_id, amount)
        return {"user_id":user_id}

    @app.route('/wallet/addBalance', methods=['POST'])
    @jwt_required()
    def add_balance():
        user_id = get_jwt_identity()
        amount = request.json['amount']
        strategy = request.json['strategy'] 
        currency = request.json['currency']
        token_wallet_dao = TokenWalletDao()
        earlier_balance = token_wallet_dao.get_wallet_balance(user_id)
        print("user_id",user_id)
        final_amt=process_payment(user_id, amount, strategy,currency)
        total = earlier_balance + int(final_amt)
        
        token_wallet_dao.update_wallet_balance(user_id, total)
        return jsonify({"status": "success"})

    @app.route('/bar/pay', methods=['POST'])
    @jwt_required()
    def pay_bar():
        user_id = get_jwt_identity()
        amount = request.json['amount']
        strategy = request.json['strategy'] 
        token_wallet_dao = TokenWalletDao()
        # earlier_balance = token_wallet_dao.get_wallet_balance(user_id)
        # total = earlier_balance + int(amount)
        process_payment(user_id, amount, strategy)
        # token_wallet_dao.update_wallet_balance(user_id, total)
        return jsonify({"status": "success"})
    
    @app.route('/wallet/addRecordBalance', methods=['POST'])
    @jwt_required()
    def add_record_balance():
        user_id = get_jwt_identity()
        print("pompom")
        amount = request.json['amount']
        strategy = request.json['strategy'] 
        currency = request.json['currency']
        casino_id = request.json['casinoId']
        token_wallet_dao = TokenWalletDao()
        earlier_balance = token_wallet_dao.get_wallet_balance(user_id)
        final_amt=process_payment(user_id, amount, strategy,currency)
        if int(amount)<0:
            token_wallet_dao.update_transaction(user_id, casino_id, final_amt, "debit")
        else:
            token_wallet_dao.update_transaction(user_id, casino_id, final_amt, "credit")

        total = earlier_balance + int(final_amt)

        token_wallet_dao.update_wallet_balance(user_id, total)
        return jsonify({"status":"success"})
