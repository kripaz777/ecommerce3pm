from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', Categories.as_view(), name='categories'),
    path('search',SearchView.as_view(), name='search'),
    path('product-details/<slug>',DetailView.as_view(), name='product-details'),
    path('reviews',review, name='reviews'),
    path('signup',signup, name='signup'),
    path('add_to_cart/<slug>',add_to_cart, name='add_to_cart'),
    path('cart/',CartView.as_view(), name='cart'),
    path('remove_cart/<slug>',remove_cart, name='remove_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
]
