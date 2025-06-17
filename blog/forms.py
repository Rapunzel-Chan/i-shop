from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'preview', 'is_published']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = 'form-control' if not isinstance(field.widget, forms.CheckboxInput) else ''
            if css:
                field.widget.attrs.update({'class': css})
