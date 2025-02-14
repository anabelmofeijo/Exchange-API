from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from playwright.sync_api import sync_playwright

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def create_database():
   with app.app_context():
      db.create_all()

 
from app.controllers import bai_controller, bic_controller, standard_controller

