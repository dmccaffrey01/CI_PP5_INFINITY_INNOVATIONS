from django.shortcuts import render, redirect, reverse, HttpResponse

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


def adjuct_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity = int(request.POST.get('quantity'))
    theme = None
    if 'product_theme' in request.POST:
        theme = request.POST['product_theme']
    cart = request.session.get('cart', {})

    if theme:
        if quantity > 0:
            cart[item_id]['items_by_theme'][theme] = quantity
        else:
            del cart[item_id]['items_by_theme'][theme]
            if not cart[item_id]['items_by_theme']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the cart """

    try:
        theme = None
        if 'product_theme' in request.POST:
            theme = request.POST['product_theme']
        cart = request.session.get('cart', {})
        print(cart[item_id]['items_by_theme'])
        print(theme)
        print(request.POST)
        if theme:
            del cart[item_id]['items_by_theme'][theme]
            print(cart[item_id]['items_by_theme'])
            if not cart[item_id]['items_by_theme']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart

        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)