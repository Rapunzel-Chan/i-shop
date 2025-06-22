from django import forms
from django.core.exceptions import ValidationError
from django.db.models import BooleanField
from django.forms import ModelForm

from .models import Contact, Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError("Название содержит запрещённые слова. Не надо так!")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError("Описание содержит запрещённые слова. Не надо так!")
        return description

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price is not None and price <= 0:
            raise ValidationError("Цена не может быть отрицательной. Бесплатно продукты тоже не отдаем.")
        return price

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        uploaded = self.files.get("photo")
        if uploaded:
            content_type = uploaded.content_type
            if content_type not in ["image/jpeg", "image/png"]:
                raise ValidationError("Можно загружать только JPEG или PNG.")
            if uploaded.size > 5 * 1024 * 1024:
                raise ValidationError("Размер должен быть ≤5 МБ.")
        return photo


# class ContactForm(ModelForm):
#     model = Contact
#     fields = ["name", "phone", "message"]
#     widgets = {
# #     name: forms.CharField(max_length=100)
# #     phone = forms.CharField(max_length=15)
# #     message = forms.CharField(widget=forms.Textarea)
