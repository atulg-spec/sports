from django.urls import path
from .views import *

urlpatterns = [
    path('', game_view, name='game_view'),
    path('<slug:slug>/', game_detail, name='game_detail'),
]

