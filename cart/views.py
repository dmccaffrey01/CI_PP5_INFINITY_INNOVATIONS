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
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect(redirect_url)
