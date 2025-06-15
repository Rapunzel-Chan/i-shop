from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect
from catalog.models import Contact, Product
from catalog.forms import ProductForm


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')



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
