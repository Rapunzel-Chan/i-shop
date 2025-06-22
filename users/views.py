from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:logout_done')
    return redirect('catalog:products_list')
