from django.contrib import admin
from orders.models import Order, OrderedItem
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'order_status', 'total_price', 'created_at')
    list_filter = ('owner','order_status', 'created_at')
    search_fields = ('owner', 'id')
    list_per_page = 10
    ordering = ('-created_at',)



admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem)