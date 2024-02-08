from django.core.management import BaseCommand

from catalog.models import Categories


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Phones', 'description':'something'},
            {'name': 'Tablets', 'description': 'something'},
            {'name': 'Laptops', 'description': 'something'},
            {'name': 'TVs', 'description': 'something'},
            {'name': 'Watches', 'description': 'something'},
        ]

        categories_for_create = []

        for category in category_list:
            categories_for_create.append(Categories(**category))

        Categories.objects.bulk_create(categories_for_create)