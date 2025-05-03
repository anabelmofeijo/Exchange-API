from playwright.sync_api import sync_playwright

class StandardScrapper:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto('https://www.standardbank.co.ao/angola/pt/Grandes-Empresas/Mercado-de-Capitais/cambios', wait_until='domcontentloaded')

    def get_coin(self) -> list:
      coins = []  

      try:
        self.page.wait_for_selector('.market-rates__table--cell__forex--details__title', state='visible')
        datas = self.page.query_selector_all('.title.title--notes.market-rates__table--cell__forex--details__currency')
        
        for data in datas:
            coin = data.inner_text().strip()
            if coin not in coins:  
                coins.append(coin[0:3])
        
        return coins  

      except Exception as e:
        print(f'Erro: {e}')
        return []

    def get_buy(self) -> list:
        all_data = []
        buy = []

        try:
            self.page.wait_for_selector('.market-rates__table--cell.market-rates__table--cell__center', state='visible', timeout=60000)
            datas = self.page.locator('.market-rates__table--cell.market-rates__table--cell__center').all_inner_texts()

            for data in datas:
                all_data.append(data)

            for i in range(2, len(all_data), 2):  
                buy.append(all_data[i])

            return buy

        except Exception as e:
            print(f'Erro ao obter dados de compra: {e}')
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
    return standard.get_coin()


if __name__ == '__main__':
    try:
        standard = main()
        print(standard)
    except Exception as e:
        print (f'Error: {e}')