from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProductForm
from catalog.models import Contact, Product
from django.core.paginator import Paginator


def products_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, 'products_list.html', context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'products_detail.html', context)


def home(request):
    latest_products = Product.objects.all().order_by("-created_at")[:5]
    return render(request, "home.html", {"latest_products": latest_products})


def contacts_view(request):
    contact = Contact.objects.first()

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        if name and phone and message:
            messages.success(request, "Спасибо! Ваше сообщение успешно отправлено.")
        return redirect("catalog:contacts")

    return render(request, "contacts.html", {"contact": contact})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:products_list')  # Заменить на нужную страницу
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
