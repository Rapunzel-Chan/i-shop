from django.core.management import BaseCommand
from django.conf import settings
from users.models import User


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         password = settings.ADMIN_PASSWORD
#         user = User.objects.create(email="admin@example.com")
#         user.is_active = True
#         user.is_staff = True
#         user.is_superuser = True
#         if created:
#             user.set_password(password)
#             user.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            email="admin@example.com",
            defaults={'is_active': True, 'is_staff': True, 'is_superuser': True}
        )
        if created:
            user.set_password(settings.ADMIN_PASSWORD)
            user.save()
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write("Admin user already exists")
