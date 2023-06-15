import os
from datetime import datetime 
from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler

from scraper.scrape import JumiaScraper
from scraper.models import Product

nairobi = timezone('Africa/Nairobi')
smartphone_url = os.getenv('JUMIA_SMARTPHONE_URL')


def save_jumia():
	try:
		jumia = JumiaScraper(smartphone_url)
		jumia_data = jumia.scrape_data()
		for data in jumia_data:
			product = Product(
			**data
			)
			product.save()  
	except Exception as e:
		print(e)
	

def jumia_scrape():
	scheduler = BackgroundScheduler()
	scheduler.add_job(save_jumia, 'cron', hour='9, 13', minute='0', timezone=nairobi)
	scheduler.start()

