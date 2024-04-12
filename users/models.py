from django.contrib.auth.models import AbstractUser
from django.db import models

from internet_shop_django.settings import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=40, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='media//', verbose_name='Аватарка', **NULLABLE)
    country = models.CharField(max_length=60, verbose_name='Страна', **NULLABLE)
    verification_code = models.CharField(max_length=20, verbose_name='Код верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []