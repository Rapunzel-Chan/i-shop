import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, UpdateView, DetailView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
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

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f'Доброго времени суток! Перейдите по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        # return super().form_valid(form)
        return render(self.request, 'users/email_verification_notice.html')


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile_edit')

    def get_object(self):
        return self.request.user
