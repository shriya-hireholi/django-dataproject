import os
from sqlalchemy_utils import drop_database
from django.core.management.base import BaseCommand
from dotenv import load_dotenv


load_dotenv()

class Command(BaseCommand):
    help = 'Insert data into models'

    def handle(self, *args, **options):
        username = os.getenv("username")
        password = os.getenv("username")
        drop_database(
            f'postgresql://{username}:{password}@localhost/django_ipl'
        )
    
        self.stdout.write(
                self.style.SUCCESS("Successfully dropped database")
            )
