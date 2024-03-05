from django.shortcuts import render, redirect
from posts.models import Product
from sales.models import Sale

# Create your views here.

def search_product(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        category_query = request.POST.get('category')

        products = Product.objects.filter(name__icontains=search_query)
        if category_query:
            products = products.filter(category=category_query)

        return render(request, 'sales/search_results.html', {'products': products, 'search_query': search_query, 'category_query': category_query})

    return render(request, 'sales/search_product.html')

def add_sale(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        quantity = int(request.POST.get('quantity'))
        Sale.objects.create(product=product, quantity=quantity)
        return redirect('search_product')

    product = Product.objects.get(pk=product_id)
    return render(request, 'sales/add_sale.html', {'product': product})