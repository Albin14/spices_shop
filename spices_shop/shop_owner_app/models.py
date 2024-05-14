# models.py

from django.db import models
from django.contrib.auth.models import User

class ShopOwner(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shop_owner_profile')
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)

    def __str__(self):
        return self.user.username

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    shop_logo = models.ImageField(upload_to='shop_logos')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

class CustomerRequest(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.item}"