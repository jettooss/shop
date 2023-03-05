from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Main_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image'].widget.attrs.update({'class': 'form-control form-control-lg'})
    class Meta:
        model = product_main
        fields = ['product', "image"]
