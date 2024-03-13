from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Users(models.Model):

    name = models.CharField(max_length=100, verbose_name='имя')
    phone = models.CharField(max_length=20, verbose_name='контакты')
    message = models.TextField(verbose_name='сообщение', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Закупается')

    def __str__(self):
        return f'{self.name} {self.phone}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('phone',)


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

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('category',)
