from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок блога"
    )
    content = models.TextField(
        verbose_name="Содержание",
        help_text="Введите содержание блога"
    )
    preview = models.ImageField(
        upload_to='blog_previews/',
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью блога"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания блога"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
        help_text="Укажите, опубликован ли блог"
    )
    views_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров блога"
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
