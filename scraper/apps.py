from django.apps import AppConfig


class ScraperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scraper'
    
    def ready(self):
        from scraper.update import jumia_scrape
        jumia_scrape()
