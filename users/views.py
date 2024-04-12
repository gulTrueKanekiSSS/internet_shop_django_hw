from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View, TemplateView, DetailView

from internet_shop_django.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User
from django.core.mail import send_mail
import random
import string

class UserDetailView(DetailView):
    model = User



class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm

    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Генерация случайного кода для верификации
        verification_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        # Отправка кода на почту
        send_mail(
            'Код верификации',
            f'Ваш код верификации: {verification_code}',
            EMAIL_HOST_USER,
            [form.cleaned_data['email']],
            fail_silently=False,
        )

        # Сохранение кода и остальных данных пользователя
        user = form.save(commit=False)
        user.verification_code = verification_code
        user.save()

        # Перенаправление на страницу с вводом кода верификации
        return redirect('users:verification', pk=user.pk)


class VerificationView(TemplateView):
    template_name = 'users/conf_email.html'

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        verification_code = request.POST.get('verification_code')

        if verification_code == user.verification_code:
            user.save()
            return redirect(reverse('users:login'))
        else:
            return redirect(reverse('users:verification', kwargs={'pk': user.pk}))


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'



class PasswordChangeDoneView(View):
    template_name = 'users/password_change_done'
