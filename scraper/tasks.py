from config.celery import app
from celery.utils.log import get_task_logger
from celery import shared_task

from scraper.scrape import JumiaScraper
from scraper.models import Product

logger = get_task_logger(__name__)

@app.task(name="scraper.jumia_scraper")
def save_scraped_data(url):
	try:
		jumia = JumiaScraper(url)
		jumia_data = jumia.scrape_data()
		for data in jumia_data:
			product = Product(
				**data
			)
			product.save()
		logger.info('Scrape and save task successful')
	except Exception as e:
		logger.info('The scraping task failed. Investigate Excepiton')
		print(e)


@shared_task
def add(x, y): 
    return x + y
