from app import app, jsonify
from app.models.bai_model import Exchange


@app.route('/bai/home/')
def home():
   return jsonify({'message':'API Rodando!'})

@app.route('/get_bai_rates/', methods=['GET'])
def get_bai_rates():
   datas = Exchange.query.filter(Exchange.bank_id==1).all()
   exchange = []
   if not datas:
      return jsonify({'message':'Not Found!'})
   for data in datas:
      exchange.append({'moeda': data.coin,'compra': data.buy,'venda': data.sell}) 
   return jsonify(exchange)

@app.route('/get_bai_rates/<int:indice>', methods=['GET'])
def get_bai_rates_by_id(indice):
   exchange_list = Exchange.query.filter(Exchange.bank_id==1).all()
   filter_exchange = []
   if not exchange_list:
      return jsonify({'message':'Not Found!'})
   for data in exchange_list:
      filter_exchange.append({'moeda': data.coin,'compra': data.buy,'venda': data.sell}) 
   return jsonify(filter_exchange[indice - 1])