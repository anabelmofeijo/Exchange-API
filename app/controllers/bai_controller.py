from app import app
from flask import jsonify
from app.models.bai_model import BankBai



@app.route('/bai/home/')
def home():
   return jsonify({'message':'API Rodando!'})

@app.route('/get_bai_rates/', methods=['GET'])
def get_bai_rates():
   datas = BankBai.query.all()
   exchange = []
   if not datas:
      return jsonify({'message':'Not Found!'})
   for data in datas:
      exchange.append({'moeda': data.moeda,'compra': data.compra,'venda': data.venda}) 
   return jsonify(exchange)

@app.route('/get_bai_rates/<int:indice>', methods=['GET'])
def get_bai_rates_by_id(indice):
   exchange = BankBai.query.get(indice)
   if exchange:
      return jsonify({'id': exchange.id, 'moeda':exchange.coin_name, 'compra':exchange.buy_list, 'venda':exchange.sell_list})
   return jsonify({'message':'Exchange Found!'})