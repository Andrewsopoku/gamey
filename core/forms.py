from django import forms

__author__ = 'andrews'

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=30 ,widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'class':"form-control"}))