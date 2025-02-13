from app import app, db
from app.scrapping.bic_scrapper import main

rates = main()

class BicBank(db.Model):
   __tablename__ = 'BIC'

   id = db.Column(db.Integer, primary_key=True)
   moeda = db.Column(db.String, nullable=False)
   compra = db.Column(db.String, nullable=False)
   venda = db.Column(db.String, nullable=False)


with app.app_context():
   db.create_all()


def database_bic():
   with app.app_context():
      try:
         for rate in rates:
            new_data = BicBank(moeda=rate['moeda'], compra=rate['compra'], venda=rate['venda'])
            db.session.add(new_data)
         db.session.commit()
         print ('Criado com sucesso! - Banco BIC')
      except Exception as e:
         print (f'Erro: {e}')
      finally:
         print ('Operação terminada com sucesso!')