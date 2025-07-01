from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView, UnpublishBlogView

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blog/<int:pk>/unpublish/", UnpublishBlogView.as_view(), name="blog_unpublish"),
]
