from config.celery import app
from celery import shared_task

from scraper.scrape import JumiaScraper
from scraper.models import Product


@app.task
def save_scraped_data(url):
	try:
		jumia = JumiaScraper(url)
		jumia_data = jumia.scrape_data()
		for data in jumia_data:
			product = Product(
				**data
			)
			product.save()
	except Exception as e:
		print('The scraping task failed. Investigate Excepiton')
		print(e)


@shared_task
def add(x, y): 
    return x + y
