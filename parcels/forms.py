from django.forms import ModelForm
from django import forms

class address(forms.Form):
    address = forms.CharField(label='address', max_length=150)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'rows':3}))