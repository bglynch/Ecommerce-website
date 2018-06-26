# /djangoecommerce/urls.py

from django.contrib import admin
from django.urls import path,include
from products import urls as products_urls
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(products_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

]
