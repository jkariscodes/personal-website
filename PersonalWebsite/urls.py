from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import PostSitemap

sitemaps = {"posts": PostSitemap}

urlpatterns = [
    path("mkubwa/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("useraccounts/", include("useraccounts.urls", namespace="useraccounts")),
    path("useraccounts/", include("allauth.urls")),
    path("", include("website.urls", namespace="website")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("summernote/", include("django_summernote.urls")),
]
