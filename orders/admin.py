from django.contrib import admin
from orders.models import Order, OrderItem

# Register your models here.

class OrderItemsAdmin(admin.ModelAdmin):
    readonly_fields = ["price"]

admin.site.register(OrderItem, OrderItemsAdmin)
admin.site.register(Order)