import time
from django.db import connections 
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
  """ 
    Pause Execution and Database is Connected
  """
  
  def handle(self, *args, **kwargs):
    self.stdout.write('Waiting for Database ...')
    db_conn = None
    while not db_conn:
      try:
        db_conn = connections['default']
      except OperationalError:
        self.stdout.write('Database unavailable, waiting 1 second...')
        time.sleep(1)
        
      self.stdout.write(self.style.SUCCESS('Database available!!!'))