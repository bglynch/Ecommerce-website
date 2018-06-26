# /products/urls.py

from django.urls import path
from .views import get_products, cart_add

urlpatterns = [
    path('cart/add', cart_add, name='cart_add'),
    path('', get_products, name='get_products'),
]