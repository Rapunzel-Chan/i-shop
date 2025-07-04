from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, ContactsView, ProductCategoryListView, ProductCreateView,
                           ProductDeleteView, ProductDetailView, ProductListView, ProductUpdateView,
                           UnpublishProductView)

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="products_detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/create/", ProductCreateView.as_view(), name="products_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"),
    path("products/<int:pk>/unpublish/", UnpublishProductView.as_view(), name="products_unpublish"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:category_id>/", ProductCategoryListView.as_view(), name="products_by_category"),
]
