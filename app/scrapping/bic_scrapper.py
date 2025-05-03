from playwright.sync_api import sync_playwright


class BicScrapper():

   def __init__(self):
      ''''''
      self.playwright = sync_playwright().start()
      self.browser = self.playwright.chromium.launch(headless=True)
      self.page = self.browser.new_page()
      try:
         self.page.goto('https://www.bancobic.ao/inicio/particulares/index', timeout=100000)
      except Exception as e:
         print (f'BIC - Erro: {e}')
      self.page.wait_for_load_state('domcontentloaded')

   def get_rates(self) -> list:
      rate_list = []
      try:
         self.page.wait_for_selector('.tab-content tr')
         rates = self.page.query_selector_all('.tab-content tr')
         for row in rates:
            columns = row.query_selector_all('td')
            if len(columns) >= 3:
               rate_dict = {
                  'coin': columns[0].inner_text().strip(),
                  'buy': columns[1].inner_text().strip(),
                  'sell': columns[2].inner_text().strip()
               }
               rate_list.append(rate_dict)
         return rate_list
      except Exception as e:
         print (f'Erro: {e}')
      finally:
         if self.browser:
            self.browser.close()
         if self.playwright:
            self.playwright.stop()

def main():
   bic = BicScrapper()
   response = bic.get_rates()
   return response

if __name__ == '__main__':
   bic = main()
   print(bic)
