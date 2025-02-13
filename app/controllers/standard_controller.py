from app import app
from flask import jsonify
from app.models.standard_model import StandardBank



@app.route('/standard/home/')
def home():
    return jsonify({'message':'API rodando'})


@app.route('/get_rates_standard/', methods=['GET'])
def get_rates_standard():
   data = StandardBank.query.all()
   exchange = []
   if not data:
         return jsonify({'message': 'Not Found'})
   for rate in data:
      exchange.append({'moeda': rate.coin_name , 'compra':rate.buy_list, 'venda':rate.sell_list})  
   return jsonify(exchange)

@app.route('/get_standard_rates/<int:indice>', methods=['GET'])
def get_standard_rates_id(indice):
    exchange = StandardBank.query.get(indice)
    if exchange:
        return jsonify({'id': exchange.id, 'moeda': exchange.coin_name, 'Compra':exchange.buy_list, 'venda': exchange.sell_list})
    return jsonify({'message': 'Exchange Found!'})

