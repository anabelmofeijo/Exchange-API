from app import  jsonify
from flask import request
from app.models.bai_model import Exchange



class BaiController:

   def __init__(self) -> None:
       self.converted_amount = None
       self.target_currency = None
       self.source_currency = None
       self.filter_target = None
       self.amount = None
       self.sell = None

   @staticmethod
   def get_rates():
      datas = Exchange.query.filter(Exchange.bank_id==1).all()
      exchange = []
      if not datas:
         return jsonify({'message':'Not Found!'}), 404
      for data in datas:
         exchange.append({'moeda': data.coin,'compra': data.buy,'venda': data.sell}) 
      return jsonify(exchange)
   
   @staticmethod
   def get_rates_id(id):
      exchange_list = Exchange.query.filter(Exchange.bank_id==1).all()
      filter_exchange = []
      if not exchange_list:
         return jsonify({'message':'Not Found!'}), 404
      for data in exchange_list:
         filter_exchange.append({'moeda': data.coin,'compra': data.buy,'venda': data.sell}) 
      return jsonify(filter_exchange[id - 1])
     
   def get_data_to_convert(self):
      self.data = request.get_json()
      self.target_currency = str(self.data.get('target_currency', '')).upper()
      self.source_currency = str(self.data.get('source_currency', '')).upper()
      self.amount = self.data.get('amount')

      if not all([self.target_currency, self.source_currency, self.amount]):
         return False, jsonify({'message': 'Missing required fields'})

      try:
         self.amount = float(self.amount)
      except (ValueError, TypeError):
         return False, jsonify({'message': 'Invalid amount'})

      if self.target_currency != 'AOA':
         self.filter_target = Exchange.query.filter(
            Exchange.bank_id == 1, Exchange.coin == self.target_currency
         ).first()
        
      else:
         self.filter_target = Exchange.query.filter(Exchange.bank_id == 1, Exchange.coin == self.source_currency).first()
         
      if not self.filter_target:
         return False, jsonify({'message': 'Currency not found'})
      
      try:
         self.sell = float(self.filter_target.sell.replace('.', '').replace(',', '.'))
      except (ValueError, AttributeError, IndentationError):
         return False, jsonify({'message': 'Invalid exchange rate'})

      return True, None

   def logic_to_convert(self):
      success, error_response = self.get_data_to_convert()
      if not success:
         return error_response

      if self.sell is None:
         return jsonify({'message': 'Exchange rate not available'}), 500

      if self.target_currency == 'AOA' and self.source_currency != 'AOA':
         self.converted_amount = self.amount * self.sell
         self.converted_amount = f'{self.converted_amount:.2f}'
      elif self.target_currency != 'AOA' and self.source_currency == 'AOA':
         self.converted_amount = self.amount / self.sell
         self.converted_amount = f'{self.converted_amount:.2f}'
      else:
         return jsonify({'message': 'Service not available'}), 410

      return jsonify({
         'target_currency': self.target_currency,
         'source_currency': self.source_currency,
         'amount': self.amount,
         'converted_amount': self.converted_amount.replace('.', ',')
      })
