from app import get_db_connection
from app import get_db_connection
from app.models.User import User
import uuid
import uuid

class UserDao:

    def get_staff_list(self, number):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT staffid FROM staff WHERE currentassignedid = '-1' ORDER BY currentassignedid LIMIT ?", (number,))
        staff_list = cursor.fetchall()
        conn.close()
        return staff_list
    
    def get_all_avail_staff(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT staffid, name FROM staff WHERE currentassignedid = '-1'")
        staff_list = cursor.fetchall()
        conn.close()
        # print("staff_list: ", staff_list)
        return staff_list
    
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
        id = "user_" + str(uuid.uuid4())
        # create a User Object
        user = User(id, username, email, age, password)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (id, username, email, age, password) VALUES (?, ?, ?, ?, ?)", (user.get_id(), user.get_username(), user.get_email(), user.get_age(), user.get_password()))
        conn.commit()
        conn.close()
        return user.get_id()
    
    def create_user_token_wallet(self, userid):
        id = "wallet_" + str(uuid.uuid4())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_token_wallet (walletid, userid, token_balance) VALUES (?, ?, ?)", (id, userid, 0))
        conn.commit()
        conn.close()
        return id
    
    def create_user_subscription(self, userid, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_subscription (userid, casinoid) VALUES (?, ?)", (userid, casinoid))
        conn.commit()
        conn.close()
        return userid
    
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
    
    def add_staff(self, name, salary):
        id = "staff_" + str(uuid.uuid4())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO staff (staffid, name, salary, currentAssignedId) VALUES (?, ?, ?, ?)", (id, name, salary, "-1"))
        conn.commit()
        conn.close()
        return id
    
    def check_user_subscription(self, userid, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_subscription WHERE userid=? AND casinoid=?", (userid, casinoid))
        user_subscription = cursor.fetchone()
        conn.close()
        if user_subscription:
            return True
        return False
    
    def check_user_subscription_by_id(self, userid, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_subscription WHERE userid=? AND casinoid=?", (userid, casinoid))
        user_subscription = cursor.fetchone()
        conn.close()
        return True if user_subscription else False
    
    def remove_user_subscription(self, userid, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user_subscription WHERE userid=? AND casinoid=?", (userid, casinoid))
        conn.commit()
        conn.close()
        return userid
    
    def get_subscribers(self, casinoid):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT userid FROM user_subscription WHERE casinoid=?", (casinoid,))
        subscribers = cursor.fetchall()
        conn.close()
        return subscribers