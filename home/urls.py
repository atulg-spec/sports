from django.urls import path
from .views import *
urlpatterns = [
    # path('', home, name='home'),
    path('register/', register, name='register'),
    path('tournaments/', tournaments, name='tournaments'),
    path('add-phone-number', add_phone_number, name='add-phone-number'),
    # path('profile/', profile, name='profile'),
    # path('games/', games, name='games'),
    # path('rules/', rules, name='rules'),
    # path('achievements/', achievements, name='achievements'),
    path('aboutus/', aboutus, name='aboutus'),
    # path('partners/', partners, name='partners'),
    path('contactus/', contactus, name='contactus'),
    path('privacypolicy/', privacypolicy, name='privacypolicy'),
    path('termsofservice/', termsofservice, name='termsofservice'),
    path('refundpolicy/', refundpolicy, name='refundpolicy'),

    # Payment Gateway
    # path('pay/', payment_view, name='payment'),
    # path('callback/', callback_view, name='callback'),
    # path('verify-payment/', redirect_page_view, name='redirect_page'),
    # # PAYMENT GATEWAY
    # path('payment/', payment_view, name='payment'),
    # path('redirect-page/', redirect_page_view, name='redirect_page'),
    # path('ads.txt', ads_txt, name='ads.txt'),
]

