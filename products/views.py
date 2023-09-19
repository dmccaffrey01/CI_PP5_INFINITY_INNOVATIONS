from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import HttpResponse



def all_products(request, type):
    """ A view to show all products, including sorting and search queries """

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


def product_detail(request, product_id):
    """ A view to show show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

