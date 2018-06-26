from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product
from django.contrib import messages


# Create your views here.
def get_products(request):
    products = Product.objects.all()
    return render(request, "products/index.html", {'products': products})
    
def cart_add(request):
    id = request.POST.get('product_id')
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)
    return HttpResponse(product.name+"added to cart")
