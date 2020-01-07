# from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ["contact_django_user"]
        labels = {
            'contact_name': "Name",
            'contact_address': "Address",
            'contact_phone': "Phone number",
            'contact_position': "Job Title",
            'contact_hospital_list': "Select Hospitals You Work With:"
        }
        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'new_contact_form'}),
            'contact_address': forms.TextInput(attrs={'class': 'new_contact_form'}),
            'contact_phone': forms.TextInput(attrs={'class': 'new_contact_form'}),
            'contact_position': forms.TextInput(attrs={'class': 'new_contact_form'}),
        }
