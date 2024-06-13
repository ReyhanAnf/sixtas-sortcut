from django import forms

class FormPredict(forms.Form):
    url = forms.CharField(
        required=False,
        widget= forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    text = forms.CharField(
    required=False,
    widget= forms.Textarea(attrs={'class': 'shadow appearance-none border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out','rows':3, 'cols':5, 'type': 'text'})
    )