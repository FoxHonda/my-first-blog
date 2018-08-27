from django import forms
from django.core.validators import validate_email
from django.core.validators import MaxLengthValidator

class ContactForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)
    message = forms.CharField(min_length=10, max_length=400,widget=forms.Textarea)

    # name = forms.CharField(widget=forms.TextInput)

    # email = forms.EmailField(widget=forms.EmailInput)

    # message = forms.CharField(widget=forms.Textarea)
