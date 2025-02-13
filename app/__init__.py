from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from playwright.sync_api import sync_playwright

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  



from app.scrapping.bai_scrapper import BaiScrapper
from app.scrapping.bic_scrapper import BicScrapper
from app.models.bai_model import BankBai
from app.controllers import bai_controller
from app.controllers import bic_controller
from app.controllers import standard_controller


