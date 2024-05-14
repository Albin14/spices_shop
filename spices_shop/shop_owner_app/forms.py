from django import forms
from .models import Shop

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'description', 'category', 'address', 'contact_number', 'email', 'shop_logo']
