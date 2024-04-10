from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Contacts(models.Model):
    name = models.CharField(max_length=110, verbose_name='имя')
    phone = models.CharField(max_length=100, verbose_name='номер телефона')
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.phone} {self.message}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Categories(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название категории")
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='media/', verbose_name='Фото', **NULLABLE)
    category_name = models.CharField(max_length=30, verbose_name="Категория", null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    price_for_unit = models.IntegerField(verbose_name='Цена за единицу товара')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата изменения', auto_now=True)
    views_counter = models.IntegerField(default=0, verbose_name='кол-во просмотров')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('category',)


class VersionProduct(models.Model):
    version_name = models.CharField(max_length=60, verbose_name='Версия продукта')
    version_num = models.CharField(max_length=150, default='1.0.0', verbose_name='Номер версии')
    is_active = models.BooleanField(default=True, verbose_name='Версия активна')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт', null=True)
    last_update = models.DateField(verbose_name='Дата применения последней версии', auto_now=True, **NULLABLE)

    class Meta:
        verbose_name = 'Версия продукта'
        verbose_name_plural = 'Версии продукта'
        ordering = ('version_num',)

