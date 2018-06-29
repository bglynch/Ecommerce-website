# /checkout/urls.py

from django.urls import path
from .views import go_to_checkout

urlpatterns = [
    path('', go_to_checkout, name='go_to_checkout'),
]
