from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('', include('django.contrib.auth.urls', namespace=None)),
    path('mkubwa/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('', include('website.urls', namespace='website')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

