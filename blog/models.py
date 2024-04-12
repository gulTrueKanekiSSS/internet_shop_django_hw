from django.db import models

from internet_shop_django.settings import NULLABLE
from users.models import User



# Create your models here.
class Poster(models.Model):
    title = models.CharField(max_length=50, verbose_name='Загаловок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='media/', verbose_name='Фото', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    creator = models.ForeignKey(User, related_name='posters', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
