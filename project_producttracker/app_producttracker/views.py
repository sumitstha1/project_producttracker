from re import template
from django.shortcuts import render

from app_producttracker.forms import ProductCreateForm
from .models import Product

# Create your views here.
def product_index(request):
    template = 'products/index.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template, context)

def product_create(request):
    create_form = ProductCreateForm()
    context = {"form": create_form}
    if request.method == 'POST':
        product = Product()

        product.title = request.POST.get('title')
        product.desc = request.POST.get('desc')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.category = request.POST.get('category')

        product.save()

        context.setdefault("msg", "Successfully Added")
        template = 'products/create.html'
        return render(request, template, context)
    template = 'products/create.html'
    return render(request, template, context)