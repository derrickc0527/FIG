from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['merchant', 'funder', 'tranDate', 'fundAmt', 'broker', 'lead', 'dealStatus', 'note']
