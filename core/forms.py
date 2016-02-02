from django.core.exceptions import ValidationError
from django import forms

from .models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    #def clean(self):
    #    if not self.is_active:
    #        raise ValidationError({'is_active': 'User must be activated'})
