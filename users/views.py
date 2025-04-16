from django.contrib.auth.decorators import login_required
from .forms import User_registration_form
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from catalog.models import Product
from .models import Cart,CartItem


def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_url')
        else:
            return render(request, 'register.html', context={
                "form": form
            })
    else:
        form = User_registration_form()
        return render(request, 'register.html', context={
               "form": form
            })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    cart_item, cart_item_created  = CartItem.objects.get_or_create(cart=cart, product=product)
    if not cart_item_created:
        cart_item.quantity +=1
        cart_item.save()
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer)

@login_required
def del_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    cart_item = cart.items.filter(product=product).first()
    if cart_item:
        cart_item.delete()
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer)

@login_required
def cart(request):
    cart, cart_created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total_sum = 0
    for item in items:
        item.total_price = item.quantity * item.product.price
        total_sum += item.total_price
    return render(request, 'cart.html', context={
        'cart_items': items,
        'total_sum': total_sum
    })