from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    ContactsView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    UnpublishProductView,
)

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    # path("home/", home, name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/create/", ProductCreateView.as_view(), name="products_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
    path("products/<int:pk>/unpublish/", UnpublishProductView.as_view(), name="products_unpublish"),
]
