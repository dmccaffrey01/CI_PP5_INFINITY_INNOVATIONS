from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(
                    request,
                    f'Updated {product.name} - {theme} theme quantity to '
                    f'{cart[item_id]["items_by_theme"][theme]}')
            else:
                cart[item_id]['items_by_theme'][theme] = quantity
                messages.success(
                    request,
                    f'Added {product.name} {theme} theme to your cart')
        else:
            cart[item_id] = {'items_by_theme': {theme: quantity}}
            messages.success(
                request, f'Added {product.name} {theme} theme to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    theme = None
    if 'product_theme' in request.POST:
        theme = request.POST['product_theme']
    cart = request.session.get('cart', {})

    if theme:
        if quantity > 0:
            cart[item_id]['items_by_theme'][theme] = quantity
            messages.success(
                request,
                f'Updated {product.name} - {theme} theme quantity to '
                f'{cart[item_id]["items_by_theme"][theme]}')
        else:
            del cart[item_id]['items_by_theme'][theme]
            if not cart[item_id]['items_by_theme']:
                cart.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name} - {theme} theme from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the cart """

    product = get_object_or_404(Product, pk=item_id)
    try:
        theme = None
        if 'product_theme' in request.POST:
            theme = request.POST['product_theme']
        cart = request.session.get('cart', {})
        if theme:
            del cart[item_id]['items_by_theme'][theme]
            if not cart[item_id]['items_by_theme']:
                cart.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name} - {theme} theme from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
