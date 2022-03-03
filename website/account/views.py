from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


class UserRegistrationView(generic.CreateView):
    """
    User creation view.
    """
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:register')


@login_required
def home(request):
    return render(request, 'website/home.html')
