from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import mysql.connector
# from config import DB_CONFIG
from config import DB_PATH
import sqlite3
#  use routes

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
    cursor.execute("CREATE TABLE IF NOT EXISTS casino (id varchar(255) PRIMARY KEY, tableid varchar(255), barid varchar(255), tokencounterid varchar(255), staffid varchar(255), managerid varchar(255))")
    conn.commit()
    cursor.execute("CREATE TABLE IF NOT EXISTS gametable (id varchar(255) PRIMARY KEY, staffid varchar(255), prob int, type varchar(255))")
    conn.commit()
    cursor.execute("CREATE TABLE IF NOT EXISTS bar (id varchar(255) PRIMARY KEY, staffid varchar(255))")
    conn.commit()
    conn.close()

create_tables()



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