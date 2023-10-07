from django.shortcuts import render, redirect
import os
from django.contrib import messages


def custom_admin(request):
    """A view to render the contact page"""
    

    return render(request, 'custom_admin/custom_admin.html')
