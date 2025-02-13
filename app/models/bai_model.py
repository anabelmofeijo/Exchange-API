from app import app, db
from app.scrapping.bai_scrapper import bai_rates

rates = bai_rates()

class BankBai(db.Model):
   ''''''
   __tablename__ = 'BAI'

   id = db.Column(db.Integer, primary_key=True)
   moeda = db.Column(db.String)
   venda = db.Column(db.String)
   compra = db.Column(db.String)

   def __repr__(self):
      return f'<Moeda {self.moeda}>'
   
with app.app_context():
   db.create_all()
 
def database_bai():
   with app.app_context():
      try:
         for rate in rates:
            new_data = BankBai(moeda=rate['moeda'], venda=rate['venda'], compra =rate['compra'])
            db.session.add(new_data)
         db.session.commit()
         print (f'Criado com sucesso! - Banco BAI')
      except Exception as e:
         print (f'ERRO: {e}')
      finally:
         print ('Operação terminada com sucesso!')






      