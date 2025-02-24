import schedule
import time
from app.scrapping.bic_scrapper import main
from app.models.bic_model import actualize_bic_database


class AtualizeBicDatabase():

   def get_new_data(self):
      actualize_bic_database()
      
   def time_to_set(self):
      schedule.every().day.at('12:00').do(self.get_new_data)
   
   @staticmethod
   def loop():
      while True:
         schedule.run_pending
         time.sleep(1)

def run_bic_task():
   set_data = AtualizeBicDatabase()
   set_data.time_to_set()
   set_data.loop()