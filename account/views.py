from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import forms
from .models import Profile


class UserRegistrationView(generic.CreateView):
    """
    User creation view.
    """
    form_class = forms.AccountRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:register-done')


class CreateProfilePageView(generic.CreateView):
    """
    Profile creation view.
    """
    model = Profile
    form_class = forms.ProfilePageForm
    template_name = 'registration/create_user_profile.html'
    success_url = reverse_lazy('account:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfileView(generic.DetailView):
    """
    Profile details of registered user.
    """
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # user_profiles = Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

    
class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = forms.ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('website:success')


class UserEditView(generic.UpdateView):
    """
    Edit user profile.
    """
    form_class = forms.ProfileEditForm
    template_name = 'registration/edit.html'
    success_url = reverse_lazy('account:dashboard')

    def get_object(self, queryset=None):
        return self.request.user


class UserLoginView(auth_views.LoginView):
    form_class = forms.UserLoginForm
    success_url = reverse_lazy('account:dashboard')


class PasswordsResetView(auth_views.PasswordResetView):
    form_class = forms.PasswordResettingForm
    success_url = reverse_lazy('account:password_reset_done')


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
