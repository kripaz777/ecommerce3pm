from django.shortcuts import render,redirect
from .views import *
from django.views.generic import View
from .models import *
# Create your views here.

class BaseView(View):
    context = {}
    context['categories'] = Category.objects.all()
    context['brands'] = Brand.objects.all()
    context['sales'] = Product.objects.filter(labels='sales')


class HomeView(BaseView):
    def get(self,request):
        self.context
        self.context['subcategories'] = SubCategory.objects.all()
        self.context['sliders'] = Slider.objects.all()
        self.context['ads'] = Ad.objects.all()
        self.context['hots'] = Product.objects.filter(labels = 'hot')
        self.context['news'] = Product.objects.filter(labels='news')
        self.context['reviews'] = Reviews.objects.all()

        return render(request,'index.html',self.context)

class Categories(BaseView):
    def get(self,request,slug):
        self.context
        ids = Category.objects.get(slug = slug).id
        self.context['category_product'] = Product.objects.filter(category_id = ids)
        return render(request,'category.html',self.context)


class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('query')
        if not query:
            return redirect('/')
        self.context['search_product'] = Product.objects.filter(name__icontains = query)
        return render(request, 'search.html', self.context)
