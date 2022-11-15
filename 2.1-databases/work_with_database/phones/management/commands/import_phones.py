import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phon = Phone(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                release_date=phone['release_date'],
                price=phone['price'],
                lte_exists=phone['lte_exists'],
                slug=phone['name'].lower().replace(' ', '-')
            )
            phon.save()

