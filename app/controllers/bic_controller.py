from app import app, jsonify
from app.models.bai_model import Exchange



@app.route('/bic/home/')
def bic_home():
   return jsonify({'message': 'API Rodando'})

@app.route('/get_bic_rates/', methods=['GET'])
def get_bic_rates():
   rates = Exchange.query.filter(Exchange.bank_id==2).all()
   exchange = []
   if not rates:
      return jsonify({'message':'Not Found!'})
   for rate in rates:
      exchange.append({'moeda':rate.coin,'compra': rate.buy,'venda': rate.sell})
   return jsonify(exchange)

@app.route('/get_bic_rates/<int:indice>', methods=['GET'])
def get_bic_rates_by_id(indice):
   rates = Exchange.query.filter(Exchange.bank_id==2).all()
   exchange = []
   if not rates:
      return jsonify({'message':'Not Found!'})
   for rate in rates:
      exchange.append({'moeda':rate.coin,'compra': rate.buy,'venda': rate.sell})
   return jsonify(exchange[indice - 1])