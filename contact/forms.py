from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Class for the Contact form model
    """
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
