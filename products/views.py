from django.shortcuts import render
from .models import Product, Category
from django.http import HttpResponse


def all_products(request, type):
    """A view to show all products, including sorting and search queries """

    if type == 'real':
        products = Product.objects.filter(category__type='real')
    elif type == 'digital':
        products = Product.objects.filter(category__type='digital')
    else:
        return HttpResponse("Invalid type parameter")



    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

