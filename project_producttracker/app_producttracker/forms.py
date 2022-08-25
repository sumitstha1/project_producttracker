from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    
    class Meta:
        fields = ('title', 'desc', 'price', 'quantity', 'category')
        model = Product