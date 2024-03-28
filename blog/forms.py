from django import forms
from django.core.exceptions import ValidationError

from blog.models import Poster


class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ('title', 'content', 'preview')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')
        arrest_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in cleaned_data.split():
            if word.lower() in arrest_words:
                raise ValidationError(f'Название продукта содержит недопустимые для публикации слова в названии - {word}')
        return cleaned_data

    def clean_content(self):
        cleaned_data = self.cleaned_data.get('content')
        arrest_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in self.cleaned_data:
            if word.lower() in arrest_words:
                raise ValidationError(f'Название продукта содержит недопустимые для публикации слова в описании- {word}')
        return cleaned_data