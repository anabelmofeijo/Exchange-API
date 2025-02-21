from app import app, db
from app.scrapping.bic_scrapper import main
from app.models.bai_model import Bank, Exchange


rates = main()

def bic_database():
   with app.app_context():
      try:
         bank = Bank(name='Banco BIC')
         db.session.add(bank)
         db.session.commit()
         print(f'{bank.name} com id: {bank.id}')
         if bank:
            for rate in rates:
               new_data = Exchange(coin=rate['moeda'], sell=rate['venda'], buy =rate['compra'], bank_id = bank.id)
               db.session.add(new_data)
            db.session.commit() 
      except Exception as e:
         print (f'Erro: {e}')
      finally:
         print (f'{bank.name} - Operação conluida!')

def actualize_bic_database():
   with app.app_context():
      try:
         bank = Bank.query.get(2) 
         if not bank:
            print("Banco não encontrado!")
            return

         exchanges = Exchange.query.filter_by(bank_id=bank.id).all() 

         for exchange, rate in zip(exchanges, rates):
            exchange.coin = rate['moeda']
            exchange.sell = rate['venda']
            exchange.buy = rate['compra']
        
         db.session.commit()  

      except Exception as e:
         print(f'Erro: {e}')
      finally:
         print('BIC - Dados atualizados com sucesso!')


      