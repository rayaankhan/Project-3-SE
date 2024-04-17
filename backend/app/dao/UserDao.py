from app import get_db_connection
from app.models.User import User
import uuid

class UserDao:
    def get_user_by_id(self, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        # convert user to User object
        if user:
            return User(*user)
        return None
    
    def get_user_by_username(self, username):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()
        # convert user to User object
        if user:
            return User(*user)
        return None
    
    def create_user(self, username, email, age, password):
        id = str(uuid.uuid4())
        # create a User Object
        user = User(id, username, email, age, password)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, username, email, age, password) VALUES (?, ?, ?, ?, ?)", (user.get_id(), user.get_username(), user.get_email(), user.get_age(), user.get_password()))
        conn.commit()
        conn.close()
        return user.get_id()
    
    def update_user(self, user_id, username=None, email=None, age=None, password=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE users SET"
        if username:
            query += " username='" + username + "',"
        if email:
            query += " email='" + email + "',"
        if age:
            query += " age=" + str(age) + ","
        if password:
            query += " password='" + password + "',"
        query = query[:-1] + " WHERE id='" + user_id + "'"
        cursor.execute(query)
        conn.commit()
        conn.close()
        return user_id

