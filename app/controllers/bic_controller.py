from app import app, jsonify
from app.models.bic_model import BicBank



@app.route('/bic/home')
def home():
   return jsonify({'message': 'API Rodando'})

@app.route('/get_bic_rates', methods=['GET'])
def get_bic_rates():
   rates = BicBank.query.all()
   exchange = []
   if not rates:
      return jsonify({'message':'Not Found!'})
   for rate in rates:
      exchange.append({'moeda':rate.moeda,'compra': rate.compra,'venda': rate.venda})
   return jsonify(exchange)

@app.route('/get_bic_rates/<int:indice>', methods=['GET'])
def get_bic_rates_by_id(indice):
   exchange = BicBank.query.get(indice)
   if exchange:
      return jsonify({'id': exchange.id, 'moeda': exchange.coin_name, 'compra':exchange.buy_list, 'venda':exchange.sell_list})
   return jsonify({'message': 'Exchange Found'})

