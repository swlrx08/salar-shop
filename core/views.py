from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.views.decorators.csrf import csrf_protect
from core.models import Product, CartOrder, CartOrderItem, Category, ProductReview, ProductImages, Address, Vendor, \
    Wishlist
from django.db.models import Count, Avg


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
    products = Product.objects.filter(category=product.category).exclude(pid=pid)

    # Getting all review
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # Getting average reviews
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    # Product Review from
    from core.forms import ProductReviewForm
    review_form = ProductReviewForm()

    p_images = product.p_images.all()

    context = {
        "product": product,
        "review_form": review_form,
        "p_images": p_images,
        "average_rating": average_rating,
        "reviews": reviews,
        "products": products,
    }

    return render(request, "main/core/product-detail.html", context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by("-id")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products": products,
        "tag": tag
    }
    return render(request, "main/core/tag.html", context)


@require_POST
@csrf_protect
def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg("rating"))

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews,
        }
    )
