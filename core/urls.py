from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.product_list_view, name="product-list"),
    path("category/", views.category_list_view, name="category-list"),
]
