from bs4 import BeautifulSoup
import requests

class CryptoCurrency:
    def __init__(self, name, url):
        self.name = name
        self.url = url 
        try:
            self.responce = requests.get(url)
            self.responce.raise_for_status()
            self.bs = BeautifulSoup(self.responce.text, "lxml")
        except requests.RequestException as err:
            print("Error fetching data: ", err)
            self.responce = None
    
    # Получить цену криптовалюты по указанному атрибуту
    def getPrice(self, attr_s):
        if self.bs is None:
            return "N/A"
        price = self.bs.find('p', attr_s)
        if price is not None:
            return price.text
        else:
            return "Price not found"
    
    # Получить цену криптовалюты по указанному атрибуту
    def getChangePrice(self, attr_s):
        if self.bs is None:
            return "N/A"
        change_price = self.bs.find('span', attr_s)
        if change_price is not None:
            return change_price.text
        else:
            return "Change price not found"
        
    # Получить Market Cup по указанному атрибуту
    def getMarketCup(self, attr_s):
        if self.bs is None:
            return "N/A"
        market_cup = self.bs.find('td', attr_s)
        if market_cup is not None:
            return market_cup.text
        else:
            return "Market Cup not found"
        
