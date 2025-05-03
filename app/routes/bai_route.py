from app import app
from app.controllers.bai_controller import BaiController



@app.route('/get_bai_rates/', methods=['GET'])
def get_bai_rates():
   bai = BaiController()
   response = bai.get_rates()
   return response

@app.route('/get_bai_rates/<string:coin>', methods=['GET'])
def get_bai_id(coin):
   bai = BaiController
   response = bai.get_rates_id(coin)
   return response

@app.route('/bai/convert/', methods=['GET'])
def bai_convert():
   bai = BaiController() 
   response = bai.logic_to_convert()
   return response