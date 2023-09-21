from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total >= settings.DISCOUNT_THRESHOLD:
        discounted_total = total - (Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100) * total)
        discount_delta = 0
    else:
        discounted_total = total
        discount_delta = settings.DISCOUNT_THRESHOLD - total

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + discounted_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'discounted_total': discounted_total,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'discount_percentage': settings.STANDARD_DISCOUNT_PERCENTAGE,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context