from app import app
from app.controllers.bic_controller import BicController


@app.route('/get_bic_rates/', methods=['GET'])
def get_bic_rates():
   bic = BicController()
   response = bic.get_rates()
   return response

@app.route('/get_bic_rates/<int:id>', methods=['GET'])
def get_bic_id(id):
   bic = BicController()
   response = bic.get_rates_id(id)
   return response

@app.route('/bic/convert/', methods=['GET'])
def bic_convert():
   bic = BicController() 
   response = bic.logic_to_convert()
   return response
