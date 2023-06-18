import os
from django.http import HttpResponse

from scraper.models import Product
from scraper.scrape import JumiaScraper

def scrape_info(request):
    try:
        jumia = JumiaScraper(os.getenv('JUMIA_SMARTPHONE_URL'))
        jumia_data =  jumia.scrape_data()
        for data in jumia_data:
            product = Product(
                **data
            )
            product.save()
    except Exception as e:
        return HttpResponse(status=404) 
    
    return HttpResponse(status=200)
