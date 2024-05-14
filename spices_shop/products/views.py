from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger    
# Create your views here.


def homepage(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    #print(context)
    return render(request, 'index.html',context)


def list_products(request):
    page=1
    if 'page' in request.GET:
        page=request.GET['page']
    else:
        page=1
        
    product_list=Product.objects.order_by('priority')
    prouduct_paginator=Paginator(product_list,2)
    product_list=prouduct_paginator.get_page(page)

    context={'products':product_list}
    return render(request, 'products.html',context)


# def search_results(request):            
#     query = request.GET['search']
#     product_list = Product.objects.filter(title__icontains=query)
#     context={'products':product_list}
#     return render(request, 'products.html',context)


def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    
    return render(request, 'product_detail.html',context)
