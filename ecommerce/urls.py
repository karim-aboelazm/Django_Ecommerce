from django.urls import path
from .views import *


app_name = 'ecommerce'

urlpatterns = [
    path(''         ,HomeView.as_view(),name='home'),
    path('men/'     ,MenView.as_view(),name='men'),
    path('woman/'   ,WomanView.as_view(),name='woman'),
    path('children/',ChildrenView.as_view(),name='children'),
    path('all-products/',AllProductsView.as_view(),name='all_products'),
    path('product-<id>-details/',ProductDetailView.as_view(),name='product_details'),
    path('client-register/',ClientRegisterView.as_view(),name='register'),
    path('client-login/',ClientLoginView.as_view(),name='login'),
    path('client-logout/',ClientLogoutView.as_view(),name='logout'),
    path('client-profile/',ClientProfileView.as_view(),name='client_profile'),
    path('client-update-profile/<int:id>',UpdateProfileView.as_view(),name='update_profile'),
    path('forget-password/',ForgotPasswordView.as_view(),name='forget_password'),
    path('reset-password/<email>/<token>/',ResetPasswordView.as_view(),name='reset_password'),
    path('add-to-cart/<int:id>',AddToCartView.as_view(),name='add_to_cart'),
    path('cart/',CartView.as_view(),name='cart'),
    path('manage-cart/<int:id>',ManageCartView.as_view(),name='manage_cart'),
    path('empty-cart/',EmptyCartView.as_view(),name='empty_cart'),
    path('checkout/',CheckoutView.as_view(),name='checkout'),
    path('payment/',PaypalAndBankView.as_view(),name='payment'),
    path('order-<int:pk>-details/',OrderDetailView.as_view(),name='order_details'),
    path('search/',SearchView.as_view(),name='search'),
]

