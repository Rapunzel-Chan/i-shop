from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts_view, home, products_list, products_detail

app_name = CatalogConfig.name
urlpatterns = [
    path("", products_list, name="products_list"),
    path("products/<int:pk>", products_detail, name="products_detail"),
    path("home/", home, name="home"),
    path("contacts/", contacts_view, name="contacts"),
]
