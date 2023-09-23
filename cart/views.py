from django.shortcuts import render, redirect

def view_cart(request):
    """ A view that renders the cart contents page """

    context = {

    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    theme = None
    if 'product_theme' in request.POST:
        theme = request.POST['product_theme']
    cart = request.session.get('cart', {})

    if theme:
        if item_id in list(cart.keys()):
            if theme in cart[item_id]['items_by_theme'].keys():
                cart[item_id]['items_by_theme'][theme] += quantity
            else:
                cart[item_id]['items_by_theme'][theme] = quantity
        else:
            cart[item_id] = {'items_by_theme': {theme: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)
