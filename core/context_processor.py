from core.models import Product, CartOrder, CartOrderItem, Category, ProductReview, ProductImages, Address, Vendor, \
    Wishlist
from django.db.models import Max, Min


def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price = Product.objects.aggregate(Min('price'), Max('price'))

    try:
        address = Address.objects.get(user=request.user)
    except:
        address = None
    return {
        'categories': categories,
        'vendors': vendors,
        'address': address,
        'min_max_price': min_max_price,
    }
