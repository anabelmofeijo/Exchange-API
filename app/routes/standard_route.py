from app import app
from app.controllers.standard_controller import StandardController


@app.route('/get_standard_rates/', methods=['GET'])
def get_standard_rates():
   standard = StandardController()
   response = standard.get_rates()
   return response

@app.route('/get_standard_rates/<string:coin>', methods=['GET'])
def get_standard_id(coin):
   standard = StandardController()
   response = standard.get_rates_id(coin)
   return response

@app.route('/standard/convert/', methods=['GET']) 
def standard_convert():
   standard = StandardController() 
   response = standard.logic_to_convert()
   return response
