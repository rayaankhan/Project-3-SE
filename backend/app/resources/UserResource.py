from flask import jsonify
from app import app
from app.models.User import User
from app import db
from app.dao.UserDao import UserDao

user_dao = UserDao()
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_dao.get_user_by_id(user_id)
    if user:
        return jsonify(user.serialize()), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/hello')
def index():
    return jsonify({"message": "Hello, World!"}), 200

@app.route('/addjohn')
def addUser():
    # Create a new user
    print('adding new user')
    new_user = User(username='john', email='john@example.com')
    print(new_user)
    db.session.add(new_user)
    db.session.commit()

    # Query all users
    users = User.query.all()
    for user in users:
        print(user)

    return 'Users added to the database'