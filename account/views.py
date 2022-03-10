from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import AccountRegistrationForm


class UserRegistrationView(generic.CreateView):
    """
    User creation view.
    """
    form_class = AccountRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:register-success')


def register_success(request):
    """
    Registration success.
    """
    return render(request, 'registration/register_done.html', {})


@login_required
def home(request):
    return render(request, 'website/home.html')


def logged_out(request):
    return render(request, 'registration/logged_out.html')
