from app import app
from flask import jsonify
from app.models.bai_model import Exchange



@app.route('/standard/home/')
def standard_home():
    return jsonify({'message':'API rodando'})


@app.route('/get_standard_rates/', methods=['GET'])
def get_standard_rates():
   data = Exchange.query.filter(Exchange.bank_id==3).all()
   exchange = []
   if not data:
         return jsonify({'message': 'Not Found'})
   for rate in data:
      exchange.append({'coin': rate.coin, 'buy':rate.buy, 'sell':rate.sell})  
   return jsonify(exchange)

@app.route('/get_standard_rates/<int:indice>', methods=['GET'])
def get_standard_rates_id(indice):
    data = Exchange.query.filter(Exchange.bank_id==3).all()
    exchange = []
    if not data:
            return jsonify({'message': 'Not Found'})
    for rate in data:
        exchange.append({'coin': rate.coin, 'buy':rate.buy, 'sell':rate.sell})  
    return jsonify(exchange[indice - 1])

