from django.core.management import BaseCommand

from catalog.models import Products


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_list = [
            {'name': 'Iphone', 'description': 'something', 'category_name': 'Phones', 'price_for_unit': 100000},
            {'name': 'Android', 'description': 'something', 'category_name': 'Phones', 'price_for_unit': 10000},
            {'name': 'Samsung', 'description': 'something', 'category_name': 'TVs', 'price_for_unit': 200000},
            {'name': 'MSI', 'description': 'something', 'category_name': 'Laptops', 'price_for_unit': 150000},
            {'name': 'AppleWatch', 'description': 'something', 'category_name': 'Watches', 'price_for_unit': 50000},
            {'name': 'Garmin', 'description': 'something', 'category_name': 'Watches', 'price_for_unit': 20000},
            {'name': 'LG', 'description': 'something', 'category_name': 'TVs', 'price_for_unit': 100000}

        ]

        products_for_create = []

        for product in products_list:
            products_for_create.append(Products(**product))

        Products.objects.bulk_create(products_for_create)
