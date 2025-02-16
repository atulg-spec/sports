from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from home.views import error_404_view, error_500_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from game.sitemaps import GameSitemap
from django.views.static import serve

sitemaps = {
    'games': GameSitemap,
}

handler404 = error_404_view
handler500 = error_500_view

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls',namespace='social')),
    path('', include('accounts.urls')),
    path('', include('home.urls')),
    path('game/', include('game.urls')),
    path('', include('game.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('ads.txt', lambda request: serve(request, path='ads.txt', document_root=settings.STATIC_ROOT)),
]
