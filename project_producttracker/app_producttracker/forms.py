from django import forms
from .models import Product, AppUser

class ProductCreateForm(forms.ModelForm):
    
    class Meta:
        fields = ('title', 'desc', 'price', 'quantity', 'category')
        model = Product

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('first_name', 'moddle_name', 'last_name', 'email', 'password')
        model = AppUser