from bs4 import BeautifulSoup
import requests 
import random

class Scraper:
    @staticmethod
    def GET_UA():
        uastrings = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",\
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"\
                ]
 
        return random.choice(uastrings)


    def __init__(self, url):
        self.url = url
        self.header = {'User-Agent': self.GET_UA()}
        self.source = requests.get(url, headers = self.header)
        self.soup = BeautifulSoup(self.source.content, 'html.parser')

    
    
class JumiaScraper(Scraper):
    def __init__(self, url):
        self.products = []
        super().__init__(url)
        
    
    def scrape_data(self):
        product_cards = self.soup.find_all("a", class_="core")
        
        for card in product_cards:
            brand = card.get('data-brand')
            name = card.get('data-name')
            category = card.get('data-category')
  
            price = card.find('div', class_='prc')
            old_price = card.find('div', class_='old')
            discount = card.find('div', class_=['_sm'])
            official = card.find('div', class_=['bdg _mall _xs'])
  
            if brand and name and price: 
                price = int(price.text.replace('KSh', '').replace(',', '')) if price else 'N/A'
                old_price = int(old_price.text.replace('KSh', '').replace(',', '')) if old_price else 'N/A'
                discount = int(discount.text.replace('%', '')) if discount else 'N/A'
                official = official.text if official else 'N/A'

                product = { 'brand' : brand,
                            'name': name,
                            'category': category, 
                            'price': price,
                            'old_price': old_price,
                            'discount': discount,
                            'official_store': official
                        }
                self.products.append(product)
        
        return self.products
    
class StandardScraper(Scraper):
    pass
