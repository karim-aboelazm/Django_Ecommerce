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
]

