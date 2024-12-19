from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('tournaments/', tournaments, name='tournaments'),
    path('games/', games, name='games'),
    path('rules/', rules, name='rules'),
    path('achievements/', achievements, name='achievements'),
    path('aboutus/', aboutus, name='aboutus'),
    path('partners/', partners, name='partners'),
    path('contactus/', contactus, name='contactus'),
    path('privacypolicy/', privacypolicy, name='privacypolicy'),
    path('termsofservice/', termsofservice, name='termsofservice'),
    path('refundpolicy/', refundpolicy, name='refundpolicy'),
]

