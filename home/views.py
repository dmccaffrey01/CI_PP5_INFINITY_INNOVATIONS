from django.shortcuts import render
from products.models import Category

def index(request):
    """A view to render the index page"""
    
    return render(request, 'home/index.html')