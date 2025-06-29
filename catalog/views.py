from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from django.views import View
from catalog.forms import ProductForm
from catalog.models import Contact, Product
from django.shortcuts import get_object_or_404, redirect


class ProductListView(ListView):
    model = Product
    # context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.has_perm('catalog.can_unpublish_product'):
            # Админ — видит всё
            return Product.objects.all()
        elif user.is_authenticated:
            # Автор — видит свои + опубликованные
            return Product.objects.filter(Q(is_published=True) | Q(owner=user))
        else:
            # Аноним — только опубликованные
            return Product.objects.filter(is_published=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


# def home(request):
#     latest_products = Product.objects.all().order_by("-created_at")[:5]
#     return render(request, "home.html", {"latest_products": latest_products})


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = Contact.objects.first()
        context["contact"] = contact
        return context

    def post(self, request, *args, **kwargs):

        name = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phone")

        if name and phone and message:
            messages.success(request, "Спасибо! Ваше сообщение успешно отправлено.")

        return redirect(reverse_lazy("catalog:contacts"))


class UnpublishProductView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'
    raise_exception = True

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        if product.is_published:
            product.is_published = False
            product.save()
            messages.success(request, f"Публикация продукта «{product.name}» отменена.")
        else:
            messages.info(request, f"Продукт «{product.name}» уже не опубликован.")
        return redirect(reverse_lazy('catalog:products_detail', kwargs={'pk': pk}))
