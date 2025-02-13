from playwright.sync_api import sync_playwright

class StandardScrapper:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto('https://www.standardbank.co.ao/angola/pt/Grandes-Empresas/Mercado-de-Capitais/cambios', wait_until='domcontentloaded')

    def get_coin(self) -> list:
      ''''''
      coins = set()
      try:
         self.page.wait_for_selector('.market-rates__table--cell__forex--details__title', state='visible')
         datas = self.page.query_selector_all('.market-rates__table--cell__forex--details__title')
         for data in datas:
            coin = data.inner_text().strip()
            coins.add(coin)
         return list(coins)

      except Exception as e:
         print(f'Erro: {e}')
         return []

    def get_buy(self) -> list:
        ''''''
        all_data = []
        buy = []
        try:
            self.page.wait_for_selector('.market-rates__table--cell.market-rates__table--cell__center', state='visible', timeout=60000)
            datas = self.page.locator('.market-rates__table--cell.market-rates__table--cell__center').all_inner_texts()
            for data in datas:
                b = data
                all_data.append(b)
            
            for i in range (2,len(all_data),2):
                data = all_data[i]
                buy.append(data)
            return buy
        
        except Exception as e:
            print(f'Erro: {e}')
            return []
    
    def get_sell(self) -> list:
        ''''''
        all_data = []
        buy = []
        try:
            self.page.wait_for_selector('.market-rates__table--cell.market-rates__table--cell__center', state='visible', timeout=60000)
            datas = self.page.locator('.market-rates__table--cell.market-rates__table--cell__center').all_inner_texts()
            for data in datas:
                b = data
                all_data.append(b)
            
            for i in range (3,len(all_data),2):
                data = all_data[i]
                buy.append(data)
            return buy
        
        except Exception as e:
            print(f'Erro: {e}')
            return []
    
    def close(self):
        self.browser.close()
        self.playwright.stop()

def main():
    standard = StandardScrapper()
    sell = standard.get_sell()
    buy = standard.get_buy()
    coin = standard.get_coin()
    print(sell)
    print(buy)
    print(coin)

def sell():
    data = StandardScrapper()
    sell = data.get_sell()
    return sell

def buy():
    data = StandardScrapper()
    buy = data.get_buy()
    return buy

def coin():
    data = StandardScrapper()
    coin = data.get_coin()
    return coin

