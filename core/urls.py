from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("products/", views.product_list_view, name="product-list"),
    path("product/<pid>/", views.product_detail_view, name="product-detail"),

    # Category
    path("category/", views.category_list_view, name="category-list"),
    path("category/<cid>/", views.category_product_list, name="category-product-list"),

    # Vendor
    path("vendors/", views.vendor_list_view, name="vendor_list"),
    path("vendor/<vid>/", views.vendor_detail_view, name="vendor_detail"),

    # tags
    path("products/tags/<slug:tag_slug>/", views.tag_list, name="tags"),

    # Add Review
    path("ajax-add-review/<pid>/", views.ajax_add_review, name='ajax-add-review'),

    # search
    path("search/", views.search_view, name="search"),

    # filter products
    path("filter-products/", views.filter_product, name="filter-product"),

    # Add to cart
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),

    # card page
    path("cart/", views.cart_view, name="cart"),

    # Delete Item From Cart
    path("delete-from-cart/", views.delete_item_from_cart, name="delete-from-cart"),

    # Update cart
    path("update-from-cart/", views.update_cart, name="update-from-cart"),

    # Check Out Page
    path("checkout/", views.checkout_view, name="checkout"),

    # Paypal
    path("paypal/", include('paypal.standard.ipn.urls')),

    # Payment Successful
    path("payment-completed/", views.payment_completed_view, name="payment-completed"),

    # Payment Failed
    path("payment-failed/", views.payment_failed_view, name="payment-failed"),

]
