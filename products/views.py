
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        from django.contrib.auth.models import User

        if User.objects.filter(username=username).exists():
            return render(request, 'products/register.html', {
                'error': 'Username already exists'
            })

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'products/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('product_list')

        return render(request, 'products/login.html', {
            'error': 'Invalid username or password'
        })

    return render(request, 'products/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products
    })

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'products/product_form.html', {
        'form': form
    })

@login_required
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_form.html', {
        'form': form
    })

@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'products/product_confirm_delete.html', {
        'product': product
    })
# Create your views here.
