from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
    path('', home),
    path('cart', cart),
    path('orders', orders),
    path('cart_offer', cart_offer),
]

