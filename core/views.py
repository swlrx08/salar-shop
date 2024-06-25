from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

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


def category_product_list(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        "category": category,
        "products": products
    }
    return render(request, "main/core/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors
    }
    return render(request, "main/core/vendor_list.html", context)


def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")
    categories = Category.objects.all()

    context = {
        'vendor': vendor,
        'products': products,
        'categories': categories,

    }
    return render(request, "main/core/vendor_detail.html", context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)

    p_images = product.p_images.all()
    products = Product.objects.filter(category=product.category).exclude(pid=pid)
    context = {
        "product": product,
        "p_images": p_images,
        "products": products,
    }

    return render(request, "main/core/product-detail.html", context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context ={
        "products": products,
        "tag": tag
    }
    return render(request, "main/core/tag.html", context)
