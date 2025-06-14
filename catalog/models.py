from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование", help_text="Ведите наименование продукта")
    description = models.TextField(verbose_name="Описание", help_text="Ведите описание продукта")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование", help_text="Введите наименование категории продуктов"
    )
    description = models.TextField(verbose_name="Описание", help_text="Введите описание категории")
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию продукта",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория", help_text="Введите категорию продукта"
    )
    price = models.FloatField(verbose_name="Цена за покупку", help_text="Введите стоимость продукта")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", help_text="Введите дату создания продукта"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения", help_text="Введите дату последнего изменения продукта"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    country = models.CharField("Страна", max_length=100)
    inn = models.CharField("ИНН", max_length=20)
    address = models.CharField("Адрес", max_length=255)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контактные данные"

    def __str__(self):
        return f"{self.country}, {self.address}"
