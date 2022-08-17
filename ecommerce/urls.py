from django.urls import path
from .views import *


app_name = 'ecommerce'

urlpatterns = [
    path(''         ,HomeView.as_view(),name='home'),
    path('men/'     ,MenView.as_view(),name='men'),
    path('woman/'   ,WomanView.as_view(),name='woman'),
    path('children/',ChildrenView.as_view(),name='children'),
    path('category/',CategoryView.as_view(),name='category'),
]

