import schedule
import time
from app.models.standard_model import actualize_standard_database


class Actualize_std_database():

   def get_new_data(self):
      actualize_standard_database()

   def time_to_set(self):
      schedule.every().day.at('12:00').do(self.get_new_data)

   @staticmethod
   def loop():
      while True:
         schedule.run_pending
         time.sleep(1)

def run_standard_task():
   set_data = Actualize_std_database()
   set_data.time_to_set()
   set_data.loop()