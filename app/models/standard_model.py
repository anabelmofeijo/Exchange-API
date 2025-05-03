from app import app, db
from app.scrapping.standard_scrapper import StandardScrapper
from app.models.bai_model import Bank, Exchange

standard = StandardScrapper()
coin_name = standard.get_coin()
buy_list = standard.get_buy()
sell_list = standard.get_sell()



def standard_database():
   ''''''
   with app.app_context():
      
      try:
         bank = Bank(name='Standard Bank')
         db.session.add(bank)
         db.session.commit()
         print (f'{bank.name} com id: {bank.id}')
         if bank:
            for coin, buy, sell in zip(coin_name, buy_list, sell_list):
               new_data = Exchange(coin = coin, buy=buy, sell=sell, bank_id=bank.id)
               db.session.add(new_data)
            db.session.commit()
      except Exception as e:
         print (f'Erro: {e}')
      finally:
         print(f'{bank.name} - Operação Concluida!')

def actualize_standard_database():
   with app.app_context():
      try:
         bank = Bank.query.get(3) 
         if not bank:
            print("Banco não encontrado!")
            return

         exchanges = Exchange.query.filter_by(bank_id=bank.id).all() 

         for exchange, coin, sell, buy in zip(exchanges, coin_name, sell_list, buy_list):
            exchange.coin = coin
            exchange.sell = sell
            exchange.buy = buy
         
         db.session.commit()
         
      except Exception as e:
         print (f'Erro: {e}')

      finally:
         print ('Standard - Dados atualizados com Sucesso!')

if __name__ == '__main__':
   actualize_standard_database()

