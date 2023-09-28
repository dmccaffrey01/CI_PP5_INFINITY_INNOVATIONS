from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    real_items_total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })

            if product.category.universe == "real":
                real_items_total += product.price
        else:
            product = get_object_or_404(Product, pk=item_id)
            for theme, quantity in item_data['items_by_theme'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'theme': theme,
                })

                if product.category.universe == "real":
                    real_items_total += product.price

    if total >= settings.DISCOUNT_THRESHOLD:
        discounted_total = total - (Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100) * total)
        discount_delta = 0
    else:
        discounted_total = total
        discount_delta = settings.DISCOUNT_THRESHOLD - total

    if real_items_total > 0:
        delivery = Decimal(settings.STANDARD_DELIVERY_COST)
    else:
        delivery = 0

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
        'real_items_total': real_items_total,
        'grand_total': grand_total,
    }

    return context