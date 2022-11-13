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
        self.context
        query = request.GET.get('query')
        if not query:
            return redirect('/')
        self.context['search_product'] = Product.objects.filter(name__icontains = query)
        return render(request, 'search.html', self.context)


class DetailView(BaseView):
    def get(self,request,slug):
        self.context
        self.context['product_details'] = Product.objects.filter(slug = slug)
        self.context['product_reviews'] =ProductReview.objects.filter(slug=slug)
        return render(request, 'product-detail.html', self.context)


def review(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        review = request.POST['review']
        slug = request.POST['slug']
        star = request.POST['star']
        data = ProductReview.objects.create(
            username = username,
            email = email,
            star = star,
            review = review,
            slug = slug
        )
        data.save()
        return redirect(f'/product-details/{{slug}}')

from django.contrib.auth.models import User
from django.contrib import messages
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'The username is already taken')
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The username is already taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                user.save()
        else:
            messages.error(request, 'The password does not match')
            return redirect('/signup')

    return render(request,'signup.html')

class Cart(BaseView):
    def get(self,request):
        self.context
        username = request.user.username
        self.context['cart_views'] = Cart.objects.filter(username = username,checkout = False)
        return render(request,'cart.html',self.context)
def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username = username,checkout = False).exists():
        quantity = Cart.objects.get(slug = slug,username = username,checkout = False).quantity
        price = Product.objects.get(slug = slug).price
        discounted_price = Product.objects.get(slug = slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        quantity = quantity+1
        total = original_price*quantity
        Cart.objects.filter(slug = slug,username = username).update(quantity = quantity,total = total)
        return redirect('/')
    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        data = Cart.objects.create(slug=slug,
                            username=username,
                            total=original_price,
                            items = Product.objects.filter(slug = slug)[0]
                            )
        data.save()
        return redirect('/')

def remove_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug = slug,username = username,checkout = False).exists():
        quantity = Cart.objects.get(slug = slug,username = username,checkout = False).quantity
        price = Product.objects.get(slug = slug).price
        discounted_price = Product.objects.get(slug = slug).discounted_price
        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        if quantity>1:
            quantity = quantity-1
        total = original_price*quantity
        Cart.objects.filter(slug = slug,username = username).update(quantity = quantity,total = total)
        return redirect('/')


def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(slug=slug, username=username,checkout = False).delete()
    return redirect('/')