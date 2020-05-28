from django.forms import ModelForm

class address(forms.Form):
    address = forms.CharField(label='address', max_length=150)
