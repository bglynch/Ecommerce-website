# /cart/views.py

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from products.models import Product
from decimal import Decimal

# Create your views here.
def get_cart(request):
    cart =  request.session.get('cart', {})
    
    cart_items = []
    cart_total=0
    items_total=0
    for p in cart:
        product = get_object_or_404(Product, pk = p)
        
        cart_item = {
            'product':product, 
            'quantity':cart[p],
            'total':Decimal(product.price*cart[p]),
        }
        
        cart_items.append(cart_item)
        cart_total += Decimal(product.price*cart[p])
        items_total += cart[p]
    
    return render(request, "cart/viewcart.html", {'cart_items': cart_items, 'cart_total':cart_total, 'items_total':items_total})
    
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