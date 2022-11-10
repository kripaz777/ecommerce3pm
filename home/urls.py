from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', Categories.as_view(), name='categories'),
    path('search',SearchView.as_view(), name='search'),
    path('product-details/<slug>',DetailView.as_view(), name='product-details'),
    path('reviews',review, name='reviews'),
]
