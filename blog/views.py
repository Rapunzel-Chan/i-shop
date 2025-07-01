# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.forms import BlogForm
from blog.models import Blog


class ContentManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Контент-менеджер").exists()


class BlogListView(ListView):
    model = Blog
    # template_name = 'blog/blog_list.html'
    # context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name="Контент-менеджер").exists():
            return Blog.objects.all()
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    # template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset=queryset)
        self.object.views_counter += 1
        self.object.save()

        if self.object.views_counter == 100:
            send_mail(
                "Поздравляем с ачивкой!",
                f'Вашу статью "{self.object.title}" прочитали 100 раз!',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
        return self.object


class BlogCreateView(LoginRequiredMixin, ContentManagerRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    # template_name = 'blog/blog_form.html'
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(LoginRequiredMixin, ContentManagerRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    # template_name = 'blog/blog_form.html'
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(LoginRequiredMixin, ContentManagerRequiredMixin, DeleteView):
    model = Blog
    # template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy("blog:blog_list")


class UnpublishBlogView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "blog.can_unpublish_blog"
    raise_exception = True

    def post(self, request, pk, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=pk)
        if blog.is_published:
            blog.is_published = False
            blog.save()
            messages.success(request, f"Публикация блога «{blog.title}» отменена.")
        else:
            messages.info(request, f"Блог «{blog.title}» уже не опубликован.")
        return redirect(reverse_lazy("blog:blog_detail", kwargs={"pk": pk}))
