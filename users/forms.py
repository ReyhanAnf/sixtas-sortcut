from django import forms
from django.contrib.auth.models import User
    
class FormProfil(forms.Form):
    jk = [
          ("Laki-Laki", "L"),
          ("Perempuan", "P")
      ]
    j = [
      ("IPA", "IPA"),
      ("IPS", "IPS")
      ]
    k = [
      ("X", "10"),
      ("XI", "11"),
      ("XII", "12")
      ]
    nis = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    jenis_kelamin = forms.ChoiceField(
        widget= forms.Select(attrs={'class': 'block text-gray-700 leading-tight mb-2 w-full text-center py-2 px-2 rounded border shadow focus:ring font-medium transform transition hover:scale-105 duration-300 ease-in-out'}),   
        choices = jk
    )
    kelas = forms.ChoiceField(
        widget= forms.Select(attrs={'class': 'block text-gray-700 mb-2 w-full text-center py-2 px-2 rounded border shadow focus:ring font-medium transform transition hover:scale-105 duration-300 ease-in-out'}),   
        choices = k
    )
    jurusan = forms.ChoiceField(
        widget= forms.Select(attrs={'class': 'block text-gray-700 mb-2 w-full text-center py-2 px-2 rounded border shadow focus:ring font-medium transform transition hover:scale-105 duration-300 ease-in-out'}),   
        choices = j
    )
    hobi = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),
        required=False
    )
    