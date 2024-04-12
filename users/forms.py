from django.contrib.auth.forms import UserCreationForm

from users.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'country', 'password1', 'password2',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
