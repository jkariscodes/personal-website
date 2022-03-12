from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    # Password change
    path('password_change/', views.PasswordsChangeView.as_view(
        template_name='registration/password_change.html'), name='password_change'),
    path('password_success/', auth_views.PasswordChangeDoneView.as_view(), name='password_success'),
    path('', include('django.contrib.auth.urls',)),
    # Password reset
    path('password_reset/', views.PasswordsResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),
    # path('password_reset_done/', views.password_reset_success, name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
]
