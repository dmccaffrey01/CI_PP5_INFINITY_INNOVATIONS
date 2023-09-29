from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm
from django.core.mail import send_mail
import os

def index(request):
    """A view to render the index page"""

    return render(request, 'home/index.html')

def policy(request):
    """A view to render the policy page"""

    return render(request, 'policy/policy.html')

def contact(request):
    """A view to render the contact page"""
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_contact_email(form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def send_contact_email(data):
    subject = 'New Contact Message'
    message = f"Name: {data['name']}\nEmail: {data['email']}\n\n{data['message']}"
    from_email = os.environ.get('EMAIL_HOST_USER')
    to_email = [os.environ.get('EMAIL_HOST_USER')]
    send_mail(subject, message, from_email, to_email)