from django.shortcuts import render

def index(request):
    """A view to render the index page"""

    return render(request, 'home/index.html')

def policy(request):
    """A view to render the policy page"""

    return render(request, 'policy/policy.html')