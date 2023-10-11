from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order, TrackingOrder


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the fomr is valid.')
    else:
        form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ Display the user's order history. """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def track_order(request, order_number):
    """ Display tracking order information """

    order = get_object_or_404(Order, order_number=order_number)
    tracking_order, created = TrackingOrder.objects.get_or_create(order=order)

    if created:
        tracking_order.save()

    current_datetime = timezone.now()

    if tracking_order.estimated_delivery < current_datetime:
        tracking_order.status = "Delivered"
        tracking_order.location = order.street_address1
        tracking_order.save()

    messages.info(request, (
        f'This is the tracking information for order {order_number}'
    ))

    template = 'tracking/tracking_order.html'

    context = {
        'order': order,
        'tracking_order': tracking_order,
    }

    return render(request, template, context)



def track_order_api(request, tracking_number):
    """ Return tracking order information for api in json response """

    order_number = tracking_number.split('_')[-1]
    order = get_object_or_404(Order, order_number=order_number)
    tracking_order, created = TrackingOrder.objects.get_or_create(order=order)

    if created:
        tracking_order.save()
    
    current_datetime = timezone.now()

    if tracking_order.estimated_delivery < current_datetime:
        tracking_order.status = "Delivered"
        tracking_order.location = order.street_address1
        tracking_order.save()

    response = {
        'tracking_number': tracking_order.tracking_number,
        'status': tracking_order.status,
        'location': tracking_order.location,
        'estimated_delivery': tracking_order.estimated_delivery,
    }

    return JsonResponse(response)