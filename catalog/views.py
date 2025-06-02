from django.shortcuts import render
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and phone and message:
            messages.success(request, "Спасибо! Ваше сообщение успешно отправлено.")

    return render(request, 'contacts.html')
