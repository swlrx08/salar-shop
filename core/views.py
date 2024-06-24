from django.http import HttpResponse
from django.shortcuts import render
from core.models import Product, CartOrder, CartOrderItem, Category, ProductReview, ProductImages, Address, Vendor, \
    Wishlist
from django.db.models import Count


def index(request):
    # products = Product.objects.all().order_by('-id')
    products = Product.objects.filter(product_status="published", featured=True)

    context = {'products': products}

    return render(request, 'main/core/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status="published")

    context = {'products': products}

    return render(request, 'main/core/product-list.html', context)


def category_list_view(request):
    # categories = Category.objects.all()
    categories = Category.objects.all().annotate(product_count=Count("category"))

    context = {
        "categories": categories
    }

    return render(request, "main/core/category-list.html", context)
