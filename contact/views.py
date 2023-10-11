from django.shortcuts import render, redirect
from django.core.mail import send_mail
import os
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """A view to render the contact page"""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_contact_email(form.cleaned_data)
            messages.success(request, 'Your message has been sent, Thank you')
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def send_contact_email(data):
    subject = 'New Contact Message'
    message = f"Name: {data['name']}\nEmail: "\
              f"{data['email']}\n\n{data['message']}"
    from_email = os.environ.get('EMAIL_HOST_USER')
    to_email = [os.environ.get('EMAIL_HOST_USER')]
    send_mail(subject, message, from_email, to_email)
