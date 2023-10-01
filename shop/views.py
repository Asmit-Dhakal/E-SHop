from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    product_objects = Product.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(name__contains=item_name)

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    products_object = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_object': products_object})


def contact(request):
    return render(request, 'shop/contact.html')


def about(request):
    product_objects = Product.objects.all()
    return render(request, 'shop/about.html', {'product_objects': product_objects})
