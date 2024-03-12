import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render

from catalog.models import Users, Products, Categories


# Create your views here.

def home(request):
    categories = list(Categories.objects.all())
    products = list(Products.objects.all())
    context = {
                "products": products,
                "categories": categories
               }
    return render(request, 'home.html', context)


def contacts(request):
    categories = list(Categories.objects.all())

    context = {
        "categories": categories
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact_information = {
                                'name': name,
                                'phone': phone,
                                'message': message
                               }
        print(contact_information)
    return render(request, 'contacts.html', context)


def product_page(request, product_id):
    product_info = Products.objects.filter(id=product_id).first()
    context = {'product_info': product_info}
    return render(request, 'product.html', context)


def go_to_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        print('OK')
        return redirect('product_page', product_id=product_id)
    return redirect('home')


def registration(request):
    categories = list(Categories.objects.all())
    context = {'categories': categories}
    return render(request, 'registartion.html', context)


def make_product(request):
    if request.method == 'POST':
        pass
    return render(request, 'create_product.html')




