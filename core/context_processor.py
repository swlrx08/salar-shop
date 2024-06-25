from core.models import Product, CartOrder, CartOrderItem, Category, ProductReview, ProductImages, Address, Vendor, \
    Wishlist


def default(request):
    categories = Category.objects.all()
    address = Address.objects.get(user=request.user)

    return {
        'categories': categories,
        'address': address
    }
