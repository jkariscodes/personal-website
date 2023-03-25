from datetime import datetime, timedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, CustomUser

today = datetime.now()
since = timedelta(days=6574)
prev_date = (today - since).date()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("username", "password")


class AccountRegistrationForm(UserCreationForm):
    """
    New user registration form.
    """

    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=50, widget=forms.TextInput())
    last_name = forms.CharField(max_length=50, widget=forms.TextInput())
    date_of_birth = forms.DateField(
        initial=prev_date,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "password1",
            "password2",
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"

    def get_object(self):
        return self.request.user


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "bio",
            "date_of_birth",
            "profile_pic",
            "website_url",
            "facebook_url",
            "twitter_url",
            "instagram_url",
            "github_url",
            "linkedin_url",
        )

    def get_object(self):
        return self.request.user


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "bio",
            "profile_pic",
            "website_url",
            "facebook_url",
            "twitter_url",
            "instagram_url",
            "github_url",
            "linkedin_url",
        )
