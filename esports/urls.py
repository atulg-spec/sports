from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from home.views import error_404_view, error_500_view
from django.conf.urls.static import static
from django.conf import settings

handler404 = error_404_view
handler500 = error_500_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls',namespace='social')),
    path('', include('accounts.urls')),
    path('', include('home.urls')),
    path('game/', include('game.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
