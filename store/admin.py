from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "icon"]
    prepopulated_fields = {"slug": ("name",)}


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ["product_name", "price", "quantity", "subtotal"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "active_price", "stock", "is_featured", "is_new", "sku"]
    list_filter = ["category", "is_featured", "is_new"]
    search_fields = ["name", "description", "brand", "sku"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["is_featured", "is_new", "stock"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["pk", "first_name", "last_name", "email", "total_amount", "status", "created_at"]
    list_filter = ["status", "created_at"]
    list_editable = ["status"]
    inlines = [OrderItemInline]


admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.site_header = "Tony Motors Admin"
admin.site.site_title = "Tony Motors"
admin.site.index_title = "Store Management"
