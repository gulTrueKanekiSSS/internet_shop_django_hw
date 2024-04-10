from django.core.management import BaseCommand

from internet_shop_django.settings import admin_password
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@gmail.com',
            first_name='Admin',
            last_name='gmail',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(admin_password)
        user.save()