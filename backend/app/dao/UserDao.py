from app.models.User import User
from app import db

class UserDao:
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def create_user(self, username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

