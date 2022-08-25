from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_index, name='product.index'),
    # path('editor/', views.product_edit, name='product.edit'),
    path('create/', views.product_create, name='product.create'),
]
