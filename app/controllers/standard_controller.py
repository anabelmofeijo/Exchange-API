from app import jsonify
from flask import request
from app.models.bai_model import Exchange



class StandardController():
     
    @staticmethod
    def get_rates():
        data = Exchange.query.filter(Exchange.bank_id==3).all()
        exchange = []
        if not data:
                return jsonify({'message': 'Not Found'})
        for rate in data:
            exchange.append({'coin': rate.coin, 'buy':rate.buy, 'sell':rate.sell})  
        return jsonify(exchange)
    
    @staticmethod
    def get_rates_id(coin):
        data = Exchange.query.filter(Exchange.bank_id==3, Exchange.coin == coin.upper()).all()
        exchange = []
        if not data:
            return jsonify({'message': 'Exchange Rate not Found!'}), 404
        for rate in data:
            exchange.append({'coin': rate.coin, 'buy':rate.buy, 'sell':rate.sell})  
        return jsonify(exchange), 200
    
    def get_data_to_convert(self):
      self.target_currency = request.args.get('target_currency', '').upper()
      self.source_currency = request.args.get('source_currency', '').upper()
      self.amount = request.args.get('amount')

      
      if not all([self.target_currency, self.source_currency, self.amount]):
         return False, jsonify({'message': 'Missing required fields'}), 400

      try:
         self.amount = float(self.amount)
      except (ValueError, TypeError):
         return False, jsonify({'message': 'Invalid amount'}), 400

      if self.target_currency != 'AOA':
         self.filter_target = Exchange.query.filter(
               Exchange.bank_id == 3, Exchange.coin == self.target_currency
         ).first()
   
      else:
         self.filter_target = Exchange.query.filter(
               Exchange.bank_id == 3, Exchange.coin == self.source_currency
         ).first()

      if not self.filter_target:
         return False, jsonify({'message': 'Currency not found'}), 404

      try:
         self.sell = float(self.filter_target.sell.replace(',', '.'))
      except (ValueError, AttributeError):
         return False, jsonify({'message': 'Invalid exchange rate'}), 500

      return True, None, 200

    def logic_to_convert(self):
     
     success, error_response, status_code = self.get_data_to_convert()
     if not success:
         return error_response, status_code

     if self.sell is None:
         return jsonify({'message': 'Exchange rate not available'}), 500

     if self.target_currency == 'AOA' and self.source_currency != 'AOA':
         self.converted_amount = self.amount * self.sell
     elif self.target_currency != 'AOA' and self.source_currency == 'AOA':
         self.converted_amount = self.amount / self.sell
     else:
         return jsonify({'message': 'Service not available'}), 410

     self.converted_amount = f'{self.converted_amount:.2f}'.replace('.', ',')

     return jsonify({
         'target_currency': self.target_currency,
         'source_currency': self.source_currency,
         'amount': self.amount,
         'converted_amount': self.converted_amount
      }), 200