# /djangoecommerce/urls.py

from django.contrib import admin
from django.urls import path,include
from products import urls as products_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('', include(products_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

]
