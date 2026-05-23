from .models import Cart, Category


def cart_context(request):
    cart_count = 0
    if request.session.session_key:
        try:
            cart = Cart.objects.get(session_key=request.session.session_key)
            cart_count = cart.item_count
        except Cart.DoesNotExist:
            pass
    categories = Category.objects.all()
    return {
        "cart_count": cart_count,
        "nav_categories": categories,
    }
