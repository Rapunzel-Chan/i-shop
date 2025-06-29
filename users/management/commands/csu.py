from django.core.management import BaseCommand
from django.conf import settings
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        password = settings.ADMIN_PASSWORD
        user = User.objects.create(email="admin@example.com")
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
