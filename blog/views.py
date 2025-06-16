
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Blog
from blog.forms import BlogForm
from django.core.mail import send_mail
from django.conf import settings

class BlogListView(ListView):
    model = Blog
    # template_name = 'blog/blog_list.html'
    #context_object_name = 'posts'
    def get_queryset(self):
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
                'Поздравляем с ачивкой!',
                f'Вашу статью "{self.object.title}" прочитали 100 раз!',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

        return self.object

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    # template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Blog
    # template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')