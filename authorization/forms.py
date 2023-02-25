from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class infoname(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name']

class CreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg'})
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            # 'password1': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),

            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),

        }