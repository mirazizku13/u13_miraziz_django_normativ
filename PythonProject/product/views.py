# from django.shortcuts import render, get_object_or_404
# from .models import Product
#
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'product/list.html', {'products': products})
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'product/detail.html', {'product': product})

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Barcha Productlarni oladi
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})