from datetime import datetime, timedelta
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User

today = datetime.now()
since = timedelta(days=6574)
prev_date = (today - since).date()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class PasswordResettingForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email',)


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class AccountRegistrationForm(UserCreationForm):
    """
    New user registration form.
    """
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(initial=prev_date, widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}
    ))

    class Meta:
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'date_of_birth',
            'password1', 
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super(AccountRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

    def get_object(self):
        return self.request.user


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('date_of_birth',)  # TODO add profile photo

