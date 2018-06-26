# /cart/urls.py

from django.urls import path
from .views import get_cart,cart_add

urlpatterns = [
    path('', get_cart, name='get_cart'),
    path('add', cart_add, name='cart_add'),
]
