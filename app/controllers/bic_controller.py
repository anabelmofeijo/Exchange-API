from app import jsonify
from app.models.bai_model import Exchange



class BicController():

   @staticmethod
   def get_rates():
      rates = Exchange.query.filter(Exchange.bank_id==2).all()
      exchange = []
      if not rates:
         return jsonify({'message':'Not Found!'})
      for rate in rates:
         exchange.append({'moeda':rate.coin,'compra': rate.buy,'venda': rate.sell})
      return jsonify(exchange)
   
   @staticmethod
   def get_rates_id(id):
      rates = Exchange.query.filter(Exchange.bank_id==2).all()
      exchange = []
      if not rates:
         return jsonify({'message':'Not Found!'})
      for rate in rates:
         exchange.append({'moeda':rate.coin,'compra': rate.buy,'venda': rate.sell})
      return jsonify(exchange[id - 1])
  
   
