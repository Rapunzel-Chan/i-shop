from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name="Зелень")

        products = [
            {"name": "Укроп", "price": 60.00, "category": category},
            {"name": "Петрушка", "price": 55.00, "category": category},
            {"name": "Базилик", "price": 70.00, "category": category},
            {"name": "Шпинат", "price": 87.00, "category": category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added product: {product.name} {product.category}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {product.name} {product.category}"))
