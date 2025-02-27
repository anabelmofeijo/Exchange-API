from app import app
from app.controllers.bic_controller import BicController


@app.route('/get_bic_rates/', methods=['GET'])
def get_bic_rates():
   bic = BicController()
   response = bic.get_rates()
   return response

@app.route('/get_bic_rates/<string:coin>', methods=['GET'])
def get_bic_id(coin):
   bic = BicController()
   response = bic.get_rates_id(coin)
   return response

@app.route('/bic/convert/', methods=['GET'])
def bic_convert():
   bic = BicController() 
   response = bic.logic_to_convert()
   return response
