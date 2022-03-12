from django.shortcuts import render
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import (
    UserLoginForm,
    PasswordChangingForm,
    PasswordResettingForm,
    AccountRegistrationForm,
    UserEditForm
)


class UserRegistrationView(generic.CreateView):
    """
    User creation view.
    """
    form_class = AccountRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:register-success')


class UserEditView(generic.UpdateView):
    """
    Edit user profile.
    """
    form_class = UserEditForm
    template_name = 'registration/edit.html'
    success_url = reverse_lazy('account:dashboard')

    def get_object(self, queryset=None):
        return self.request.user


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    success_url = reverse_lazy('account:dashboard')


class PasswordsChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('account:password_success')


class PasswordsResetView(auth_views.PasswordResetView):
    form_class = PasswordResettingForm
    success_url = reverse_lazy('website:home')

def change_password_success(request):
    return render(request, 'registration/password_change_done.html', {})


def user_register_success(request):
    return render(request, 'registration/register_done.html', {})


def password_reset_success(request):
    return render(request, 'registration/password_reset_done.html', {})


def register_success(request):
    """
    Registration success.
    """
    return render(request, 'registration/register_done.html', {})


@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html')


def logged_out(request):
    return render(request, 'registration/logged_out.html')
