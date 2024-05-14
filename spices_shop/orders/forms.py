from django import forms
from .models import ProductItem

class ProductForm(forms.Form):
    class Meta:
        model = ProductItem
        fields = ['name', 'quantity', 'price_per_unit', 'count']
        