from app import jsonify
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
    def get_rates_id(id):
        data = Exchange.query.filter(Exchange.bank_id==3).all()
        exchange = []
        if not data:
            return jsonify({'message': 'Not Found'})
        for rate in data:
            exchange.append({'coin': rate.coin, 'buy':rate.buy, 'sell':rate.sell})  
        return jsonify(exchange[id - 1])

