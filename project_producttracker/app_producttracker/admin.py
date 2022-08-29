from encodings import search_function
from django.contrib import admin

from .models import AppUser, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'price', 'quantity', 'category')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category') 


admin.site.register(AppUser)
admin.site.register(Product, ProductAdmin)