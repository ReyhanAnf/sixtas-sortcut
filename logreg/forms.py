from django import forms
from django.contrib.auth.models import User
    
class FormLogin(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out'}),
    )
    
class FormRegister(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out'}),
    )
    confirm_password = forms.CharField(
        widget= forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out'}),
    )
    first_name = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'})
    )
    last_name = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),
    )
    email = forms.EmailField(
        widget= forms.TextInput(attrs={'id':'email-form','class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),
        required= False
    )
    