from django.shortcuts import render, redirect
from .models import Review
from django.views.decorators.http import require_POST
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    """A view to render the index page"""

    return render(request, 'home/index.html')


def policy(request):
    """A view to render the policy page"""

    return render(request, 'policy/policy.html')


def reviews(request):
    """A view to render the reviews page"""

    reviews = Review.objects.all()

    context = {
        'reviews': reviews
    }

    return render(request, 'reviews/reviews.html', context)


@require_POST
@csrf_exempt
def add_review_api(request):
    """ Add a review api call """
    api_key = request.META.get('HTTP_REVIEW_POST_API_KEY')

    if api_key == os.environ.get(
            'REVIEW_POST_API_KEY') and request.method == 'POST':
        message = request.POST.get('message')

        if message:
            review = Review.objects.create(message=message)
            review.save()
            response_data = {"status": "Message received", "message": message}
            return JsonResponse(response_data)
        else:
            return JsonResponse({"status": "Message is missing"}, status=400)
    else:
        return JsonResponse({"status": "Invalid API"}, status=400)
