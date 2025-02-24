from app import app
from app.controllers.bai_controller import BaiController



@app.route('/get_bai_rates/', methods=['GET'])
def get_bai_rates():
   bai = BaiController()
   response = bai.get_rates()
   return response

@app.route('/get_bai_rates/<int:id>', methods=['GET'])
def get_bai_id(id):
   bai = BaiController
   response = bai.get_rates_id(id)
   return response

@app.route('/bai/convert/', methods=['GET'])
def bai_convert():
   bai = BaiController()
   bai.get_data_to_convert()
   response = bai.logic_to_convert()
   return response