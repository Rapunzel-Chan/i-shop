from django.urls import path

from blog.apps import BlogConfig
# from blog.views import

app_name = BlogConfig.name

urlpatterns = [
    # path("blog/", ProductListView.as_view(), name="products_list"),
    # path("catalog/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    # # path("home/", home, name="home"),
    # path("contacts/", ContactsView.as_view(), name="contacts"),
    # path('catalog/create', ProductCreateView.as_view(), name='products_create'),
]