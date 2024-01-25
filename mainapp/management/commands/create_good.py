from django.core.management.base import BaseCommand
from mainapp.models import Good


class Command(BaseCommand):
    help = "Create good."

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('price')
        parser.add_argument('count')

    def handle(self, *args, **kwargs):
        good = Good(name=kwargs['name'], price=kwargs['price'], count=kwargs['count'])
        good.save()
        self.stdout.write(f'{good}')