from .models import Cart


def cart_context(request):
    if not request.user.is_authenticated:
        return {
            'number': 0,
        }
    else:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()
        number = len(items)
        return {'number': number}
