from django.shortcuts import render, get_object_or_404
from cart.forms import Add2CartForm
from shop.models import Product, Category


def home(request, slug=None):
    products = Product.objects.filter(status=True)
    categories = Category.objects.filter()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = Add2CartForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})
