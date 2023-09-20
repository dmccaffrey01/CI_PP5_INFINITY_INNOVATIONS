from django.shortcuts import render

def view_cart(request):
    """ A view that renders the cart contents page """

    context = {

    }

    return render(request, 'cart/cart.html', context)
