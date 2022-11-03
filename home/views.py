from django.shortcuts import render
from .views import *
from django.views.generic import View
from .models import *
# Create your views here.

class BaseView(View):
    context = {}


class HomeView(BaseView):
    def get(self,request):
        self.context['categories'] = Category.objects.all()
        self.context['subcategories'] = SubCategory.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['ads'] = Ad.objects.all()
        self.context['brands'] = Brand.objects.all()
        self.context['hots'] = Product.objects.filter(labels = 'hot')
        self.context['news'] = Product.objects.filter(labels='news')
        self.context['sales'] = Product.objects.filter(labels='sales')
        self.context['reviews'] = Reviews.objects.all()

        return render(request,'index.html',self.context)

