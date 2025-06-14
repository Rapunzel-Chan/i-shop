from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts_view, home, products_list

app_name = CatalogConfig.name
urlpatterns = [
    path("", products_list),
    path("home/", home, name="home"),
    path("contacts/", contacts_view, name="contacts"),
]
