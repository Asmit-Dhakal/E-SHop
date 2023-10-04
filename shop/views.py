from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, order, OrderUpdate
from users.models import Contact
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
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone_number', '')
        desc = request.POST.get('desc', '')
        contacts = Contact(name=name, email=email, phone_number=phone_number, desc=desc)
        contacts.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank': thank})
    return render(request, 'shop/contact.html')


def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        item_json = request.POST.get('itemsJson', '')

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        province = request.POST.get('province', '')
        district = request.POST.get('district', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip', '')
        # Create and save the Order object within the POST block
        orders = order(item_json=item_json, name=name, email=email, phone=phone, province=province, district=district,
                       city=city, zip_code=zip_code)
        orders.save()
        update = OrderUpdate(order_id=orders.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = orders.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')


def tracker(request):
    return render(request, 'shop/tracking.html')


def about(request):
    product_objects = Product.objects.all()
    return render(request, 'shop/about.html', {'product_objects': product_objects})
