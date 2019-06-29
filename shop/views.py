from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product,Subcategory

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def cart(request):
    return render(request, 'shop/cart.html')

def categories(request):
    category = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/categories.html', {'category': category,'products': products,})


def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    return render(request, 'shop/contact.html')

def product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'shop/product.html',{'product':product})

def allproducts(request, pk):

    products = Product.objects.all()
    category = Category.objects.get(pk=pk)
    subcategory = Subcategory.objects.filter(category = category)
    #subcategory = Subcategory.objects.get(id=args)
    #subcategory = Subcategory.objects.filter(categories = args)
    #print("args are", args)
    #print(kargs)
    return render(request, 'shop/allproducts.html',{'products':products, 'subcategory':subcategory, 'category':category})


# Create your views here.
