# /cart/urls.py

from django.urls import path
from .views import get_cart,cart_add, cart_remove

urlpatterns = [
    path('', get_cart, name='get_cart'),
    path('add', cart_add, name='cart_add'),
    path('remove', cart_remove, name='cart_remove'),
]
