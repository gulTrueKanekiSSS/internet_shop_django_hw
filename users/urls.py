from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import RegisterView, VerificationView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [

    path('register/', RegisterView.as_view(template_name='users/registration.html'), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check_code/<int:pk>/', VerificationView.as_view(), name='verification'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

