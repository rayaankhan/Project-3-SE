from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
#  use routes

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =f'mysql+pymysql://root:adminpassword@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.models.User import User

with app.app_context():
    # Create all tables
    print('Creating all tables...')
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

from app.resources.UserResource import *