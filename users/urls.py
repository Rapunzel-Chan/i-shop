from django.urls import path

from users.apps import UsersConfig
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from users.views import logout_view, UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout/done/', TemplateView.as_view(template_name='users/logout.html'), name='logout_done'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
]
