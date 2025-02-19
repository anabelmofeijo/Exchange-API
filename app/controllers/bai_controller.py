from app import  jsonify
from flask import request
from app.models.bai_model import Exchange



class BaiController:

   @staticmethod
   def get_rates():
      datas = Exchange.query.filter(Exchange.bank_id==1).all()
      exchange = []
      if not datas:
         return jsonify({'message':'Not Found!'})
      for data in datas:
         exchange.append({'moeda': data.coin,'compra': data.buy,'venda': data.sell}) 
      return jsonify(exchange)
   
   @staticmethod
   def get_rates_id(id):
      exchange_list = Exchange.query.filter(Exchange.bank_id==1).all()
      filter_exchange = []
      if not exchange_list:
         return jsonify({'message':'Not Found!'})
      for data in exchange_list:
         filter_exchange.append({'moeda': data.coin,'compra': data.buy,'venda': data.sell}) 
      return jsonify(filter_exchange[id - 1])
   
   @staticmethod
   def convert_currency():
      data = request.get_json()
      target_currency = str(data.get('target_currency'))
      source_currency = str(data.get('source_currency'))
      amount = float(data.get('amount'))
      filter_target = Exchange.query.filter(Exchange.bank_id==1,Exchange.coin==target_currency).first()

      if not target_currency:
         return jsonify({"message": "Target currency not found!"})

      if filter_target:
         sell = float(filter_target.sell.replace(',', '.'))
         converted_amount = amount / sell
         return jsonify({"target_currency": target_currency, "source_currency":source_currency, 'converted_amount':converted_amount})

