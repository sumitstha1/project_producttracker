from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from app_producttracker.forms import ProductCreateForm, UserCreateForm
from .models import Product
from django.core.mail import send_mail
import random
import string

# Create your views here.

def generate_random_string(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def user_register(request):
    template = 'users/register.html'
    user_create_form = UserCreateForm
    if request.method == "POST":
        user = UserCreateForm(request.POST)
        user.save()

        chars = string.ascii_letters + string.punctuation
        size = 4

        verification_code = generate_random_string(size, chars)
        
        send_mail(
            'User Verification',
            'Your verification code is: ' + verification_code,
            'edchristian.inventor@gmail.com',
            [request.POST.get('email')]
        )

        return render(request, template)
    context = {'form': user_create_form}
    return render(request, template, context)


def product_index(request):
    template = 'products/index.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template, context)

def product_show(request, id):
    product = Product.objects.get(id=id)
    template = 'products/show.html'
    context = {"product": product}
    return render(request, template, context)

def product_edit(request, id):
    product = Product.objects.get(id=id)
    template = 'products/edit.html'
    context = {"product": product}
    return render(request, template, context)

def product_update(request):
    
    if request.method == 'POST':
        product = Product.objects.get(id=request.POST.get('id'))

        product.title = request.POST.get('title')
        product.desc = request.POST.get('desc')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.category = request.POST.get('category')
        product.user_id = 1

        product.save()
        return redirect("product.index")
    return redirect("product.index")

def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return redirect('product.index')



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