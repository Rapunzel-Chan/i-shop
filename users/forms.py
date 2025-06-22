from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin
from users.models import User
from django import forms


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone', 'avatar', 'country']


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
