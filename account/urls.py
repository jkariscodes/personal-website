from django.urls import path, include
from .views import (
    UserRegistrationView, 
    register_success, 
    dashboard, 
    logged_out,
    UserEditView,
)

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register_success/', register_success, name='register-success'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logged_out/', logged_out, name='logged_out'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
]
