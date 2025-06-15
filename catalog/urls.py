from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import add_product, ContactsView, ProductListView, ProductDetailView, ContactsView

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>", ProductDetailView.as_view(), name="products_detail"),
    # path("home/", home, name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path('add/', add_product, name='add_product'),
]
