from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts_view, home, index

app_name = CatalogConfig.name
urlpatterns = [
    path("", index),
    path("home/", home, name="home"),
    path("contacts/", contacts_view, name="contacts"),
]
