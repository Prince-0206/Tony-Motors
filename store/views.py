from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Category, Product, Cart, CartItem, Order, OrderItem


def get_or_create_cart(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    cart, _ = Cart.objects.get_or_create(session_key=session_key)
    return cart


def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_featured=True, stock__gt=0)[:8]
    new_products = Product.objects.filter(is_new=True, stock__gt=0)[:4]
    all_products = Product.objects.filter(stock__gt=0)[:12]
    context = {
        "categories": categories,
        "featured_products": featured_products,
        "new_products": new_products,
        "all_products": all_products,
    }
    return render(request, "store/home.html", context)


def products(request):
    category_slug = request.GET.get("category")
    search_query = request.GET.get("q", "")
    sort_by = request.GET.get("sort", "newest")

    product_list = Product.objects.filter(stock__gt=0)
    categories = Category.objects.all()
    active_category = None

    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        product_list = product_list.filter(category=active_category)

    if search_query:
        product_list = product_list.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(brand__icontains=search_query) |
            Q(compatibility__icontains=search_query)
        )

    sort_map = {
        "newest": "-created_at",
        "price_low": "price",
        "price_high": "-price",
        "name": "name",
    }
    product_list = product_list.order_by(sort_map.get(sort_by, "-created_at"))

    context = {
        "products": product_list,
        "categories": categories,
        "active_category": active_category,
        "search_query": search_query,
        "sort_by": sort_by,
        "total_count": product_list.count(),
    }
    return render(request, "store/products.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related = Product.objects.filter(category=product.category, stock__gt=0).exclude(pk=product.pk)[:4]
    context = {
        "product": product,
        "related_products": related,
    }
    return render(request, "store/product_detail.html", context)


def cart_view(request):
    cart = get_or_create_cart(request)
    context = {"cart": cart}
    return render(request, "store/cart.html", context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = get_or_create_cart(request)
    quantity = int(request.POST.get("quantity", 1))

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.save()

    messages.success(request, f'"{product.name}" added to cart.')
    next_url = request.POST.get("next", request.META.get("HTTP_REFERER", "/cart/"))
    return redirect(next_url)


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect("cart")


def update_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    quantity = int(request.POST.get("quantity", 1))
    if quantity < 1:
        item.delete()
        messages.success(request, "Item removed from cart.")
    else:
        item.quantity = quantity
        item.save()
    return redirect("cart")


def checkout(request):
    cart = get_or_create_cart(request)
    if not cart.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect("cart")

    if request.method == "POST":
        order = Order.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            zip_code=request.POST.get("zip_code"),
            total_amount=cart.total,
            notes=request.POST.get("notes", ""),
        )
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                product_name=cart_item.product.name,
                price=cart_item.product.active_price,
                quantity=cart_item.quantity,
            )
        cart.items.all().delete()
        messages.success(request, f"Order #{order.pk} placed successfully! We'll contact you shortly.")
        return redirect("order_success", order_id=order.pk)

    context = {"cart": cart}
    return render(request, "store/checkout.html", context)


def order_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, "store/order_success.html", {"order": order})


def about(request):
    return render(request, "store/about.html")


def contact(request):
    if request.method == "POST":
        messages.success(request, "Thank you for your message! We'll get back to you within 24 hours.")
        return redirect("contact")
    return render(request, "store/contact.html")
