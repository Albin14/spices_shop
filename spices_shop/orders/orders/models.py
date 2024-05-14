from django.db import models
from customers.models import Customer
from products.models import Product
# Model for orders


class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DISPATCHED = 3
    ORDER_DELIVERED = 4
    ORDER_CANCELLED = 5

    ORDER_STATUS_CHOICES = ((ORDER_CONFIRMED, 'Order Confirmed'),
                            (ORDER_PROCESSED, 'Order Processed'),
                            (ORDER_DISPATCHED, 'Order Dispatched'),
                            (ORDER_DELIVERED, 'Order Delivered'),
                            (ORDER_CANCELLED, 'Order Cancelled'))
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=CART_STAGE)
    # owner= models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True)
    total_price= models.FloatField(default=0)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)

    def __str__(self):
        return "order-{}-{}".format(self.id, self.owner.user.username)
    
class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='added_items', null=True)
    count = models.IntegerField(default=1)
    quantity=models.CharField(max_length=10, choices=[('grams', 'Grams'), ('kilos', 'Kilos')])
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_items', null=True)
