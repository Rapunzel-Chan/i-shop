from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


@csrf_protect
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:logout_done')
    return redirect('catalog:products_list')


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
