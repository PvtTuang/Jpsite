from django.shortcuts import render
from posts.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home/home.html',{'products':products})

