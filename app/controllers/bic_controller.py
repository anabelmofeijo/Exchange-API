from app import jsonify
from flask import request
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
         self.filter_target = Exchange.query.filter(Exchange.bank_id == 2, Exchange.coin == self.source_currency).first()
         
      if not self.filter_target:
         return False, jsonify({'message': 'Currency not found'})
      
      try:
         self.sell = float(self.filter_target.sell)
      except (ValueError, AttributeError):
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

   
