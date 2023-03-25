from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "useraccounts"

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path(
        "register_done/", views.UserRegisterSuccessView.as_view(), name="register-done"
    ),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("edit_profile/", views.UserEditView.as_view(), name="edit_profile"),
    path(
        "edit_profile/success/",
        views.UserEditSuccessView.as_view(),
        name="edit_profile_success",
    ),
    path("profile/<int:pk>/", views.ShowProfileView.as_view(), name="user_profile"),
    path(
        "edit_profile/<int:pk>/",
        views.EditProfilePageView.as_view(),
        name="edit_user_profile",
    ),
    path(
        "create_profile/",
        views.CreateProfilePageView.as_view(),
        name="create_user_profile",
    ),
    path("api/v1/", views.UsersAPIView.as_view()),
    path("api/v1/login/", views.MyTokenObtainPairView.as_view()),
    path("api/v1/token/refresh/", TokenRefreshView.as_view()),
]
