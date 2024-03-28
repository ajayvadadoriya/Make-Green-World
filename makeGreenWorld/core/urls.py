from django.urls import path
from core.views import index
from core.views import about
from core.views import product_list_view,delete_item_from_cart,add_to_cart,cart_view,product_category_list_view,product_detail_view,ajax_add_review,search_view,filter_product
from core.views import checkout

app_name="core"

urlpatterns=[
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("shop/",product_list_view,name="product"),
    path("product/<pid>/",product_detail_view,name="product-detail"),
    path("subcategory/<sid>",product_category_list_view,name="product-category-list"),
    path("check-out/",checkout,name="checkout"),
    path("ajax-add-review/<pid>/", ajax_add_review, name="ajax-add-review"),
    path("search/", search_view, name="search"),
    path("filter-product/",filter_product,name="filter-product"),
    path("add-to-cart/",add_to_cart,name="add-to-cart"),
    path("cart/",cart_view,name="cart"),
    path("delete-from-cart/",delete_item_from_cart,name="delete-from-cart"),
]