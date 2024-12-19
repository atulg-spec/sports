from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from home.views import error_404_view, error_500_view

handler404 = error_404_view
handler500 = error_500_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls',namespace='social')),
    path('', include('accounts.urls')),
    path('', include('home.urls')),
]

