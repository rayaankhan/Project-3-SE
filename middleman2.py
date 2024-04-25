from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

PAYMENT_BACKEND_URL = 'http://localhost:5001'
OTHER_BACKEND_URL = 'http://localhost:8080'

# Define routes dictionary
routes = {
    '5000': {'GET': [], 'POST': []},
    '6000': {'GET': [], 'POST': []}
}

# Populate routes dictionary
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

# Dynamically register routes
for port, methods in routes.items():
    for method, routes_list in methods.items():
        for route in routes_list:
            # Define route handler function dynamically
            def route_handler(route=route, port=port, method=method):
                backend_url = PAYMENT_BACKEND_URL if port == '5000' else OTHER_BACKEND_URL
                url = f"{backend_url}{route}"
                if method == 'GET':
                    response = requests.get(url, params=request.args)
                elif method == 'POST':
                    response = requests.post(url, json=request.json, headers={'Content-Type': 'application/json'})
                return response.text, response.status_code

            # Register route dynamically
            if method == 'GET':
                app.route(route, methods=[method])(route_handler)
            elif method == 'POST':
                app.route(route, methods=[method])(route_handler)

# Route for index
@app.route('/')
def index():
    # Redirect to the frontend running on port 3000
    return redirect(url_for('static', filename='index.html'))

if __name__ == '__main__':
    app.run(port=5000)
