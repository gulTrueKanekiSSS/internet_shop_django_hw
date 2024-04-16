from django.core.cache import cache

from internet_shop_django import settings
from catalog.models import Categories


def get_cached_categories_for_product(product_id: int):
    if settings.CACHE_ENABLED:
        key = f'categories_list_{product_id}'
        categories_list = cache.get(key)
        if categories_list is None:
            categories_list = Categories.objects.filter(product_id=product_id)
            cache.set(key, categories_list)
    else:
        categories_list = Categories.objects.filter(product_id=product_id)
    return categories_list