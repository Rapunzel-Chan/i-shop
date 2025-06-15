from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Contact, Product

from .forms import ProductForm

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# class ProductDetailView(DetailView):
#     model = Product



# def products_list(request):
#     catalog = Product.objects.all()
#     paginator = Paginator(catalog, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {"page_obj": page_obj}
#
#     return render(request, 'products_list.html', context)


# def home(request):
#     latest_products = Product.objects.all().order_by("-created_at")[:5]
#     return render(request, "home.html", {"latest_products": latest_products})


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = Contact.objects.first()
        context['contact'] = contact
        return context

    def post(self, request, *args, **kwargs):

        name = request.POST.get("name")
        message = request.POST.get("message")
        phone = request.POST.get("phone")

        if name and phone and message:
            messages.success(request, "Спасибо! Ваше сообщение успешно отправлено.")

        return redirect(reverse_lazy("catalog:contacts"))


# def contacts_view(request):
#     contact = Contact.objects.first()
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         if name and phone and message:
#             messages.success(request, "Спасибо! Ваше сообщение успешно отправлено.")
#         return redirect("catalog:contacts")
#
#     return render(request, "contacts.html", {"contact": contact})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:products_list')  # Заменить на нужную страницу
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
