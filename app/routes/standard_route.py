from app import app
from app.controllers.standard_controller import StandardController


@app.route('/get_standard_rates/', methods=['GET'])
def get_standard_rates():
   standard = StandardController()
   response = standard.get_rates()
   return response

@app.route('/get_standard_rates/<int:id>', methods=['GET'])
def get_standard_id(id):
   standard = StandardController()
   response = standard.get_rates_id(id)
   return response

@app.route('/standard/convert/', methods=['GET']) 
def standard_convert():
   standard = StandardController() 
   response = standard.logic_to_convert()
   return response
