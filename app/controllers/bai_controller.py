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
         exchange.append({'coin': data.coin,'buy': data.buy,'sell': data.sell}) 
      return jsonify(exchange)
   
   @staticmethod
   def get_rates_id(coin):
      exchange_list = Exchange.query.filter(Exchange.bank_id==1, Exchange.coin == coin.upper()).all()
      filter_exchange = []
      if not exchange_list:
         return jsonify({'message':'Not Found!'}), 404
      for data in exchange_list:
         filter_exchange.append({'coin': data.coin,'buy': data.buy,'sell': data.sell}) 
      return jsonify(filter_exchange), 200
     
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
            Exchange.bank_id == 1, Exchange.coin == self.target_currency
        ).first()
    else:
        self.filter_target = Exchange.query.filter(
            Exchange.bank_id == 1, Exchange.coin == self.source_currency
        ).first()

    if not self.filter_target:
        return False, jsonify({'message': 'Currency not found'}), 404

    try:
        self.dots = self.filter_target.sell.count('.')
        self.comma = self.filter_target.sell.count(',')
        if self.dots and self.comma:
           self.sell = float(self.filter_target.sell.replace('.', '').replace(',', '.'))
        else:
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
