# """
# Ai Application - MoKH
# """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime as dt
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)

# # create DB if not exists
# def create_database():
#     try:
#         engine = SQLAlchemy.create_engine('mysql://mohan@localhost:3306') # connect to server
#         conn = engine.connect()
#         conn.execute("commit")
#         conn.execute("CREATE DATABASE ai_chat") #create db
#         conn.execute("USE ai_chat") # select new db
#         conn.close()

#     except Exception as e:
#         print("An error occurred:", e)

from app.models import Interactions, Mappings, History
# Create the table if not exists
with app.app_context():
    db.create_all()


from app import routes

