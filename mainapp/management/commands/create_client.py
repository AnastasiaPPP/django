from django.core.management.base import BaseCommand
from mainapp.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        user = Client(name='John', email='john@example.com', phone_number='233322', address='street1')
        user.save()
        self.stdout.write(f'{user}')
