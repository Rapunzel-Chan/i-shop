from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import add_product, contacts_view, home, products_detail, products_list

app_name = CatalogConfig.name
urlpatterns = [
    path("", products_list, name="products_list"),
    path("products/<int:pk>", products_detail, name="products_detail"),
    path("home/", home, name="home"),
    path("contacts/", contacts_view, name="contacts"),
    path('add/', add_product, name='add_product'),
]
