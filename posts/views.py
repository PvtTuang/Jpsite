from django.shortcuts import render, redirect
from posts.models import Product
from posts.forms import ProductForm 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request,'posts/product_list.html',{'products':products})

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'posts/product_detail.html',{'product':product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'posts/product_form.html', {'form': form})

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'posts/product_form.html', {'form': form})

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    image_paths = [
        os.path.join(settings.MEDIA_ROOT, str(product.image1)),
        os.path.join(settings.MEDIA_ROOT, str(product.image2)),
        os.path.join(settings.MEDIA_ROOT, str(product.image3)),
    ]
    if request.method == 'POST':
        product.delete()
        for path in image_paths:
            if FileSystemStorage().exists(path):
                FileSystemStorage().delete(path)
        return redirect('product_list')
    return render(request, 'posts/product_delete.html', {'product': product})

def product_search(request):
    search_query = request.POST.get('search')
    category_query = request.POST.get('category')

    if search_query or category_query:
        product_name = Q(name__icontains=search_query)
        category = Q(category__icontains=category_query)

        products = Product.objects.filter(product_name & category)
    else:
        products = Product.objects.all()

    return render(request, 'home/home.html', {'products': products, 'search_query': search_query})