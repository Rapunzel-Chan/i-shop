from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name='Модератор продуктов')
        perms = Permission.objects.filter(
            codename__in=['can_unpublish_product', 'delete_product']
        )
        group.permissions.set(perms)
        self.stdout.write(
            self.style.SUCCESS('Назначены права группе "Модератор продуктов"')
        )
