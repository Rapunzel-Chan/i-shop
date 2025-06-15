from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import add_product, contacts_view, home, ProductListView, ProductDetailView

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>", ProductDetailView.as_view(), name="products_detail"),
    path("home/", home, name="home"),
    path("contacts/", contacts_view, name="contacts"),
    path('add/', add_product, name='add_product'),
]
