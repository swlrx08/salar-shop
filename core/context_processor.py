from django.contrib import messages

from core.models import Product, CartOrder, CartOrderItem, Category, ProductReview, ProductImages, Address, Vendor, \
    Wishlist
from django.db.models import Max, Min


def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price = Product.objects.aggregate(Min('price'), Max('price'))

    try:
        wishlist = Wishlist.objects.filter(user=request.user)
    except:
        messages.warning(request, "You need to login before accessing wishlist")
        wishlist = 0
    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None
    return {
        'categories': categories,
        'vendors': vendors,
        'address': address,
        'min_max_price': min_max_price,
        'wishlist': wishlist,
    }
