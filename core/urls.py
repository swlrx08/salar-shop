from django.urls import path
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

]
