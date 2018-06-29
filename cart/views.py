# /cart/views.py

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from products.models import Product
from decimal import Decimal
from .utils import get_cart_items_and_total

# Create your views here.
def get_cart(request):
    cart =  request.session.get('cart', {})
    context= get_cart_items_and_total(cart)
    return render(request, "cart/viewcart.html", context)
    
def cart_add(request):
    # Get the product were adding
    
    id = request.POST.get('product_id')
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product, pk=id)
    
    # Get the current cart
    cart = request.session.get('cart', {})
    
    # Update the cart
    cart[id] = cart.get(id, 0) + 1
    
    # Save the cart back to the session
    request.session['cart'] = cart
    
    # Redirect to somewhere
    return HttpResponse(cart[id])
    
def cart_remove(request):
    id = request.POST.get('product_id')
    product = get_object_or_404(Product, pk=id)
    cart = request.session.get('cart', {})
    if cart.get(id) > 1:
       cart[id] = cart.get(id, 0) + -1
    else:
        del cart[id]
    request.session['cart'] = cart
    return redirect('get_cart')