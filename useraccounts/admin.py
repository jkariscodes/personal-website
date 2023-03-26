from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserEditForm
from .models import Profile, CustomUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "bio",
        "date_of_birth",
        "profile_pic",
    ]


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserEditForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "date_of_birth",
                    "facebook_url",
                    "website_url",
                    "twitter_url",
                    "instagram_url",
                    "github_url",
                    "linkedin_url",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "date_of_birth",
                    "facebook_url",
                    "website_url",
                    "twitter_url",
                    "instagram_url",
                    "github_url",
                    "linkedin_url",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
