from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

PAYMENT_BACKEND_URL = 'http://localhost:5001'
OTHER_BACKEND_URL = 'http://localhost:8080'

@app.route('/users/login', methods=['POST'])
def handle_payment():
    print("hello")
    # Forward the payment request to the payment backend
    payment_response = requests.post('http://localhost:8080/users/login', json=request.json,headers={'Content-Type': 'application/json'})
    print(payment_response.json())
    return payment_response.json(), payment_response.status_code

@app.route('/other-routes', methods=['GET', 'POST'])
def handle_other_routes():
    # Forward the request to the other backend
    other_response = requests.get(f'{OTHER_BACKEND_URL}/other-routes', params=request.args)
    return other_response.text, other_response.status_code

@app.route('/')
def index():
    # Redirect to the frontend running on port 3000
    return redirect(url_for('static', filename='index.html'))

if __name__ == '__main__':
    app.run(port=5000)

routes = {
    '5000': {'GET': [], 'POST': []},
    '6000': {'GET': [], 'POST': []}
}

routes['5000']['GET'] = [
    '/users/<int:user_id>',
    '/wallet/balance'
]

routes['5000']['POST'] = [
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

routes['6000']['GET'] = [
    '/wallet/balance'
]

routes['6000']['POST'] = [
    "/check_subscription",
    '/get_user_notifications',
    '/wallet/update',
    '/wallet/addBalance'
]