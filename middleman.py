from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# PAYMENT_BACKEND_URL = 'http://localhost:5001'
# OTHER_BACKEND_URL = 'http://localhost:8080'

# @app.route('/users/login', methods=['POST'])
# def handle_payment():
#     print("hello")
#     # Forward the payment request to the payment backend
#     payment_response = requests.post('http://localhost:8080/users/login', json=request.json,headers={'Content-Type': 'application/json'})
#     print(payment_response.json())
#     return payment_response.json(), payment_response.status_code

# @app.route('/other-routes', methods=['GET', 'POST'])
# def handle_other_routes():
#     # Forward the request to the other backend
#     other_response = requests.get(f'{OTHER_BACKEND_URL}/other-routes', params=request.args)
#     return other_response.text, other_response.status_code

# @app.route('/')
# def index():
#     # Redirect to the frontend running on port 3000
#     return redirect(url_for('static', filename='index.html'))



routes = {
    '5001': {'GET': [], 'POST': []},
    '8080': {'GET': [], 'POST': []}
}

routes['5001']['GET'] = [
    '/users/<int:user_id>',
    '/wallet/balance'
]

routes['5001']['POST'] = [
    '/casino/add',
    '/manager_casinos',
    '/all_casinos',
    '/casino_info',
    '/gametable_info',
    '/bar_info',
    '/add_gametable_bar',
    '/update_gametable_staff',
    '/update_bar_staff',
    '/delete_casino',
    '/delete_gametable',
    '/delete_bar',
    '/play',
    '/notify',
    '/manager/add',
    '/users/add',
    '/subscribe',
    '/users/login',
    '/avail_staff',
    '/add_staff',
    "/check_subscription",
    '/get_user_notifications',
    '/wallet/update',
    '/wallet/addBalance'
]

routes['8080']['GET'] = [
    '/wallet/balance'
]

routes['8080']['POST'] = [
    "/check_subscription",
    '/get_user_notifications',
    '/wallet/update',
    '/wallet/addBalance'
]


# i want that all the requests at the route 5000/ are redirected to this function
@app.route('/')
def handleRoutes():
    print("hello")
    return {'hey': 'there'}

# PAYMENT_BACKEND_URL = 'http://localhost:5001'
# OTHER_BACKEND_URL = 'http://localhost:8080'

# @app.route('/users/login', methods=['POST'])
# def handle_payment():
#     print("hello")
#     # Forward the payment request to the payment backend
#     payment_response = requests.post('http://localhost:8080/users/login', json=request.json,headers={'Content-Type': 'application/json'})
#     print(payment_response.json())
#     return payment_response.json(), payment_response.status_code

# @app.route('/other-routes', methods=['GET', 'POST'])
# def handle_other_routes():
#     # Forward the request to the other backend
#     other_response = requests.get(f'{OTHER_BACKEND_URL}/other-routes', params=request.args)
#     return other_response.text, other_response.status_code


routes = {
    '5001': {'GET': [], 'POST': []},
    '8080': {'GET': [], 'POST': []}
}

routes['5001']['GET'] = [
    '/users/<int:user_id>',
    '/wallet/balance'
]

routes['5001']['POST'] = [
    '/casino/add',
    '/manager_casinos',
    '/all_casinos',
    '/casino_info',
    '/gametable_info',
    '/bar_info',
    '/add_gametable_bar',
    '/update_gametable_staff',
    '/update_bar_staff',
    '/delete_casino',
    '/delete_gametable',
    '/delete_bar',
    '/play',
    '/notify',
    '/manager/add',
    '/users/add',
    '/subscribe',
    '/users/login',
    '/avail_staff',
    '/add_staff',
    "/check_subscription",
    '/get_user_notifications',
    '/wallet/update',
    '/wallet/addBalance'
]

routes['8080']['GET'] = [
    '/wallet/balance'
]

routes['8080']['POST'] = [
    "/check_subscription",
    '/get_user_notifications',
    '/wallet/update',
    '/wallet/addBalance'
]

@app.route('/users/<int:user_id>',methods=['GET'])
def handle_user_id():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.get('http://localhost:5001/users/<int:user_id>', params=request.args)
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/casino/add', methods=['POST'])
def handle_casino_add():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/casino/add', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/manager_casinos', methods=['POST'])
def handle_manager_casinos():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/manager_casinos', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/all_casinos', methods=['POST'])
def handle_all_casinos():
    print("hello")
    # Forward the payment request to the payment backend
    print(request.headers['Authorization'])
    payment_response = requests.post('http://localhost:5001/all_casinos',headers={'Content-Type': 'application/json', 'Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/casino_info', methods=['POST'])
def handle_casino_info():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/casino_info', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/gametable_info', methods=['POST'])
def handle_gametable_info():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/gametable_info', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/bar_info', methods=['POST'])
def handle_bar_info():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/bar_info', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/add_gametable_bar', methods=['POST'])
def handle_add_gametable_bar():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/add_gametable_bar', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/update_gametable_staff', methods=['POST'])
def handle_update_gametable_staff():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/update_gametable_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/update_bar_staff', methods=['POST'])
def handle_update_bar_staff():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/update_bar_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/delete_casino', methods=['POST'])
def handle_delete_casino():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/delete_casino', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/delete_gametable', methods=['POST'])
def handle_delete_gametable():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/delete_gametable', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/delete_bar', methods=['POST'])
def handle_delete_bar():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/delete_bar', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/play', methods=['POST'])
def handle_play():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/play', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/notify', methods=['POST'])
def handle_notify():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/notify', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/manager/add', methods=['POST'])
def handle_manager_add():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/manager/add', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/users/add', methods=['POST'])
def handle_users_add():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/users/add', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/subscribe', methods=['POST'])
def handle_subscribe():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/subscribe', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/users/login', methods=['POST'])
def handle_users_login():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/users/login', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
    
@app.route('/avail_staff', methods=['POST'])
def handle_avail_staff():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/avail_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/add_staff', methods=['POST'])
def handle_add_staff():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/add_staff', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route("/check_subscription", methods=['POST'])
def handle_check_subscription():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/check_subscription', json=request.json,headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/get_user_notifications', methods=['POST'])
def handle_get_user_notifications():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:5001/get_user_notifications', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/wallet/balance',methods=['POST'])
def handle_payment():
    print("hello")
    # user_id = request.args.get('user_id')
    # Forward the payment request to the payment backend
    print(request.headers['Authorization'])
    payment_response = requests.post('http://localhost:8080/wallet/balance', headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/wallet/update',methods=['POST'])
def handle_wallet_update():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:8080/wallet/update', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code
@app.route('/wallet/addBalance',methods=['POST'])
def handle_wallet_addBalance():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:8080/wallet/addBalance', json=request.json,headers={'Content-Type': 'application/json','Authorization': request.headers['Authorization']})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code




if __name__ == '__main__':
    app.run(port=5000)