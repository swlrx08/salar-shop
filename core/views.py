from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product, CartOrder, CartOrderItem, Category, ProductReview, ProductImages, Address, Vendor, \
    Wishlist


def index(request):
    products = Product.objects.all().order_by('-id')

    context = {'products': products}

    return render(request, 'main/core/index.html', context)
