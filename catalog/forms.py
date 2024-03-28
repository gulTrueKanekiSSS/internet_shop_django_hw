from django import forms
from django.core.exceptions import ValidationError

from .models import Products, Contacts, VersionProduct


class StyleMixinForm:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleMixinForm, forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description', 'image', 'price_for_unit',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        arrest_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in cleaned_data.split():
            if word.lower() in arrest_words:
                raise ValidationError(f'Название продукта содержит недопустимые для публикации слова в названии - {word}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        arrest_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in self.cleaned_data:
            if word.lower() in arrest_words:
                raise ValidationError(f'Название продукта содержит недопустимые для публикации слова в описании- {word}')
        return cleaned_data


class ContactForm(StyleMixinForm, forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'phone', 'message',)



