from django.urls import path
from .views import CategoryList, ProductList, ProductDetail, OrderCreate, OrderList, OrderDetail, InvoicePDF, ProfileView, PromoList, PromoDetail, WishlistList, WishlistCreate, WishlistDelete

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('orders/', OrderCreate.as_view(), name='order-create'),
    path('orders/list/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('orders/<int:pk>/invoice/', InvoicePDF.as_view(), name='order-invoice'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Promo endpoints
    path('promos/', PromoList.as_view(), name='promo-list'),
    path('promos/<str:code>/', PromoDetail.as_view(), name='promo-detail'),

    # Wishlist endpoints
    path('wishlist/', WishlistList.as_view(), name='wishlist-list'),
    path('wishlist/add/', WishlistCreate.as_view(), name='wishlist-add'),
    path('wishlist/remove/<int:product_id>/', WishlistDelete.as_view(), name='wishlist-remove'),
]
