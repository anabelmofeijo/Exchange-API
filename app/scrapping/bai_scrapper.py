from playwright.sync_api import sync_playwright

class BaiScrapper():
   ''''''
   def __init__(self) -> None:
      ''''''
      self.playwright = sync_playwright().start()
      self.browser = self.playwright.chromium.launch(headless=True)
      self.page = self.browser.new_page()
      self.page.goto ('https://www.bancobai.ao/pt/cambios-e-valores')
      self.page.wait_for_load_state('networkidle')
              
   def get_rates(self) -> None:
      ''''''
      rate_list = []
      try:
         self.page.wait_for_selector('.table-striped tr')
         rates = self.page.query_selector_all('.table-striped tr')
         for row in rates:
            columns = row.query_selector_all('td')
            if len(columns)>=4:
               rate_dict = {
                  'moeda' : columns[0].inner_text().strip().replace('\n', ' '),
                  'venda' : columns[1].inner_text().strip(),
                  'compra' : columns[2].inner_text().strip(), 
               }
               rate_list.append(rate_dict)
         return rate_list
      finally:
         if self.browser:
            self.browser.close()
         if self.playwright:
            self.playwright.stop()

def bai_rates ():
   bai = BaiScrapper()
   rates = bai.get_rates()
   return rates
   
   