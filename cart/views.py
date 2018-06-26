# /cart/views.py

from django.shortcuts import render, HttpResponse, get_object_or_404
from products.models import Product

# Create your views here.
def get_cart(request):
    return render(request, "cart/viewcart.html")
    
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