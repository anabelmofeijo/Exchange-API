import schedule
import time
from app.scrapping.bai_scrapper import bai_rates
from app.models.bai_model import actualize_bai_database


class ActualizaDatabase():

   def get_new_data(self):  
      actualize_bai_database()
    
   def time_to_set(self):
      schedule.every().day.at('12:00').do(self.get_new_data)

   @staticmethod
   def loop():
      while True:
         schedule.run_pending()
         time.sleep(1)

def run_bai_task():
   set_data = ActualizaDatabase()
   set_data.time_to_set()
   set_data.loop()




   
