from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

PAYMENT_BACKEND_URL = 'http://localhost:8080'
OTHER_BACKEND_URL = 'http://localhost:5001'

# i want that all the requests at the route 5000/ are redirected to this function
@app.route('/')
def handleRoutes():
    print("hello")
    return {'hey': 'there'}

@app.route('/users/<int:user_id>',methods=['GET'])
def handle_user_id():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.get(f'{OTHER_BACKEND_URL}/users/<int:user_id>', params=request.args)
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/casino/add', methods=['POST'])
def handle_casino_add():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/casino/add', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/manager_casinos', methods=['POST'])
def handle_manager_casinos():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/manager_casinos', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/all_casinos', methods=['POST'])
def handle_all_casinos():
    print("hello")
    # Forward the payment request to the payment backend
    print(request.headers['Authorization'])
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/all_casinos',headers={'Content-Type': 'application/json', 'Authorization': request.headers['Authorization']})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/casino_info', methods=['POST'])
def handle_casino_info():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/casino_info', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/gametable_info', methods=['POST'])
def handle_gametable_info():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/gametable_info', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/bar_info', methods=['POST'])
def handle_bar_info():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/bar_info', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/add_gametable_bar', methods=['POST'])
def handle_add_gametable_bar():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/add_gametable_bar', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/update_gametable_staff', methods=['POST'])
def handle_update_gametable_staff():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/update_gametable_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/update_bar_staff', methods=['POST'])
def handle_update_bar_staff():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/update_bar_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/delete_casino', methods=['POST'])
def handle_delete_casino():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/delete_casino', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/delete_gametable', methods=['POST'])
def handle_delete_gametable():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/delete_gametable', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/delete_bar', methods=['POST'])
def handle_delete_bar():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/delete_bar', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/play', methods=['POST'])
def handle_play():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/play', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/notify', methods=['POST'])
def handle_notify():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/notify', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/manager/add', methods=['POST'])
def handle_manager_add():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/manager/add', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/users/add', methods=['POST'])
def handle_users_add():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/users/add', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/subscribe', methods=['POST'])
def handle_subscribe():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/subscribe', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/users/login', methods=['POST'])
def handle_users_login():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/users/login', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
    
@app.route('/avail_staff', methods=['POST'])
def handle_avail_staff():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/avail_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/add_staff', methods=['POST'])
def handle_add_staff():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/add_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route("/check_subscription", methods=['POST'])
def handle_check_subscription():
    print("hello")
    # Forward the payment request to the payment backend
    non_non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/check_subscription', json=request.json,headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(non_non_payment_response.json())
    return non_non_payment_response.json(), non_non_payment_response.status_code
@app.route('/get_user_notifications', methods=['POST'])
def handle_get_user_notifications():
    print("hello")
    # Forward the payment request to the payment backend
    non_payment_response = requests.post(f'{OTHER_BACKEND_URL}/get_user_notifications', json=request.json,headers={'Content-Type': 'application/json'})
    print(non_payment_response.json())
    return non_payment_response.json(), non_payment_response.status_code
@app.route('/wallet/balance',methods=['POST'])
def handle_payment():
    print("hello")
    # user_id = request.args.get('user_id')
    # Forward the payment request to the payment backend
    print(request.headers['Authorization'])
    payment_response = requests.post(f'{PAYMENT_BACKEND_URL}/wallet/balance', headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/wallet/addRecordBalance',methods=['POST'])
def handle_addRecordBalance():
    print("hello")
    # user_id = request.args.get('user_id')
    # Forward the payment request to the payment backend
    # print(request.headers['Authorization'])
    payment_response = requests.post(f'{PAYMENT_BACKEND_URL}/wallet/addRecordBalance', json=request.json,headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/wallet/update',methods=['POST'])
def handle_wallet_update():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post(f'{PAYMENT_BACKEND_URL}/wallet/update', json=request.json,headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/wallet/addBalance',methods=['POST'])
def handle_wallet_addBalance():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post(f'{PAYMENT_BACKEND_URL}/wallet/addBalance', json=request.json,headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code

if __name__ == '__main__':
    app.run(port=5000)