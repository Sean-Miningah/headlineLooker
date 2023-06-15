from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
	""" 
		Create SuperUser with Admin credentials
	"""
	
	def add_arguments(self, parser):
		parser.add_argument('--username', type=str, help='Admin username')
		parser.add_argument('--email', type=str, help='Admin email')
		parser.add_argument('--password', type=str, help='Admin password')
  
	def handle(self, *args, **options):
		username = options['username']
		password = options['password']
		email = options['email']
  
		User = get_user_model()
		if username and password and email:
			if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
				User.objects.create_superuser(username=username, password=password, email=email)
				self.stdout.write(self.style.SUCCESS('Admin user created successfully.'))
			else:
				self.stdout.write(self.style.WARNING('Admin user already exists.'))
		else:
			self.stdout.write(self.style.ERROR('Please provide --username, --password, and --email arguments.'))