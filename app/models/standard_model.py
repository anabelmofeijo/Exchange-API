from app import app, db
from app.scrapping.standard_scrapper import StandardScrapper

standard = StandardScrapper()
coin_name = standard.get_coin()
buy_list = standard.get_buy()
sell_list = standard.get_sell()

class StandardBank(db.Model):
   __tablename__ = 'STANDARD'

   id = db.Column(db.Integer, primary_key = True)
   coin_name = db.Column(db.String, nullable = False)
   buy_list = db.Column(db.String, nullable = False)
   sell_list = db.Column(db.String, nullable = False)


with app.app_context():
   db.create_all()
   

def database():
   ''''''
   with app.app_context():
      try:
         for coin, buy, sell in zip(coin_name, buy_list, sell_list):
            new_data = StandardBank(coin_name = coin, buy_list=buy, sell_list=sell)
            db.session.add(new_data)
         db.session.commit()
         print('Criado com sucesso - Standard Bank!')
      except Exception as e:
         print (f'Erro: {e}')
      finally:
         print('Operação terminada com sucesso!')


