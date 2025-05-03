from app import app, db
from app.scrapping.bai_scrapper import bai_rates

def scrapper():
   rates = bai_rates()
   return rates


class Bank(db.Model):
   __tablename__ = 'bank'

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   exchange = db.relationship('Exchange', backref='bank')

class Exchange(db.Model):
   ''''''
   __tablename__ = 'exchange'

   id = db.Column(db.Integer, primary_key=True)
   coin = db.Column(db.String)
   sell = db.Column(db.String)
   buy = db.Column(db.String)
   bank_id = db.Column(db.Integer, db.ForeignKey('bank.id'))

   def __repr__(self):
      return f'<Moeda {self.moeda}>'
   


def bai_database():
   rates = scrapper()
   with app.app_context():
      try:
         bank = Bank(name='Banco BAI')
         db.session.add(bank)
         db.session.commit()
         print(f'{bank.name} com id: {bank.id}')

         if bank:
            for rate in rates:
               new_data = Exchange(coin=rate['coin'], sell=rate['sell'], buy =rate['buy'], bank_id = bank.id)
               db.session.add(new_data)
            db.session.commit() 

      except Exception as e:
         print (f'Erro: {e}')
      finally:
         print (f'{bank.name} - Operação conluida!')

def actualize_bai_database():
   rates = scrapper()
   with app.app_context():
      try:
         bank = Bank.query.get(1) 
         if not bank:
            print("Banco não encontrado!")
            return

         exchanges = Exchange.query.filter_by(bank_id=bank.id).all() 

         for exchange, rate in zip(exchanges, rates):
            exchange.coin = rate['coin']
            exchange.sell = rate['sell']
            exchange.buy = rate['buy']
        
         db.session.commit()  

      except Exception as e:
         print(f'Erro: {e}')
      finally:
         print('BAI - Dados atualizados com sucesso!')

if __name__ == '__main__':
   actualize_bai_database()
