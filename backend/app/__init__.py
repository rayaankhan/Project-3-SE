from flask import Flask
from flask_cors import CORS
import os
import mysql.connector
# from config import DB_CONFIG
from config import DB_PATH
import sqlite3
import mysql.connector
# from config import DB_CONFIG
from config import DB_PATH
import sqlite3
import uuid

app = Flask(__name__)
CORS(app)

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    # create your tables here
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id varchar(255) PRIMARY KEY, username varchar(255), email varchar(255), age int, password varchar(255))")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS \"transaction\" (txnid varchar(255) PRIMARY KEY, paymenttype varchar(255), amount int)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS gametable (gametableid varchar(255) PRIMARY KEY, name varchar(255), staffid varchar(255), prob int, type varchar(255), FOREIGN KEY (staffid) REFERENCES staff(id) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS bar (barid varchar(255) PRIMARY KEY, name varchar(255), staffid varchar(255), drinks int)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS staff (staffid varchar(255) PRIMARY KEY, name varchar(255), salary int, currentassignedid varchar(255), FOREIGN KEY (currentassignedid) REFERENCES gametable(gametableid) ON DELETE CASCADE, FOREIGN KEY (currentassignedid) REFERENCES bar(barid) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS casino_token_mg (casinoid varchar(255) PRIMARY KEY, casinoname varchar(255), tokencountername varchar(255), tokencounterid varchar(255), managerid varchar(255), FOREIGN KEY (managerid) REFERENCES users(id) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS casino_gametable (casinoid varchar(255), gametableid varchar(255) PRIMARY KEY, FOREIGN KEY (casinoid) REFERENCES casino_token_mg(casinoid) ON DELETE CASCADE, FOREIGN KEY (gametableid) REFERENCES gametable(gametableid) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS casino_bar (casinoid varchar(255), barid varchar(255) PRIMARY KEY, FOREIGN KEY (casinoid) REFERENCES casino_token_mg(casinoid) ON DELETE CASCADE, FOREIGN KEY (barid) REFERENCES bar(barid) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS txn_user_casino (txnid varchar(255), userid varchar(255), casinoid varchar(255), FOREIGN KEY (userId) REFERENCES users(id) ON DELETE CASCADE, FOREIGN KEY (casinoId) REFERENCES casino_token_mg(casinoid) ON DELETE CASCADE, FOREIGN KEY (txnId) REFERENCES \"transaction\"(txnid) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS txn_tokencounter (txnid varchar(255) PRIMARY KEY, tokencounterid varchar(255), FOREIGN KEY (tokencounterid) REFERENCES casino_token_mg(tokencounterid) ON DELETE CASCADE, FOREIGN KEY (txnid) REFERENCES \"transaction\"(txnid) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS casino_analytics (casinoid varchar(255), gametableid varchar(255), datetime varchar(255), amount int, FOREIGN KEY (casinoId) REFERENCES casino_token_mg(casinoid) ON DELETE CASCADE, FOREIGN KEY (gametableId) REFERENCES casino_gametable(gametableid) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS user_token_wallet (walletid varchar(255) PRIMARY KEY, userid varchar(255), token_balance int, FOREIGN KEY (userid) REFERENCES users(id) ON DELETE CASCADE)")
    conn.commit()

    cursor.execute("CREATE TABLE IF NOT EXISTS user_subscription (casinoid varchar(255), userid varchar(255), FOREIGN KEY (casinoid) REFERENCES casino_token_mg(casinoid) ON DELETE CASCADE, FOREIGN KEY (userid) REFERENCES users(id) ON DELETE CASCADE)")
    conn.commit()
    
    conn.close()

create_tables()
# addStaff()


if __name__ == '__main__':
    app.run(debug=True)

# db = sqlite3.connect(DB_PATH)

# cursor = db.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS users (id varchar(255) PRIMARY KEY, username varchar(255), email varchar(255), age int, password varchar(255))")
# db.commit()


# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] =f'mysql+pymysql://root:adminpassword@localhost:3306/db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# print("hi")
# db = mysql.connector.connect(**DB_CONFIG)
# print("hi1")
# # 

# # create tables in database from app.models import User
# import app.models.User
# db.create_all()
from app.resources.UserResource import *
from app.resources.ManagerResource import *
from app.resources.CasinoResource import *
from app.resources.TokenWalletResource import *
from app.models.builder.ConcreteStrategy import *