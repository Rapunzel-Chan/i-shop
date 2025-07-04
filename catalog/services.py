from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Функция сервисного слова для запроса списка продуктов из кэша"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category_id(category_id):
    """Возвращает список опубликованных продуктов по категории с кэшированием."""

    if not category_id:
        return Product.objects.none()

    key = f"product_list_category_id_{category_id}"
    products = cache.get(key)

    if products is None:
        queryset = Product.objects.filter(category_id=category_id, is_published=True)
        products = list(queryset)
        cache.set(key, products, timeout=60)

    return products
