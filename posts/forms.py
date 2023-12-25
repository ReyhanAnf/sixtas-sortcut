from django import forms
from django.contrib.auth.models import User



class FormPost(forms.Form):
    author_id = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow bg-gray-700 border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    content_post = forms.CharField(
        widget= forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500', 'type': 'text'}),   
    )
    image_post = forms.ImageField(
        widget= forms.FileInput(attrs={'id':'dropzone-files','class': 'hidden', 'type': 'file', 'value':'image.jpg'}),   
    )
    


class FormAnswer(forms.Form):
    post_id = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow bg-gray-700 border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    answerer_id = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow bg-gray-700 border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    content_answer = forms.CharField(
        widget= forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500', 'type': 'text'}),   
    )
    

class FormReply(forms.Form):
    answer_id = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow bg-gray-700 border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    replier_id = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'shadow bg-gray-700 border rounded w-full p-3 text-gray-700 leading-tight focus:ring transform transition hover:scale-105 duration-300 ease-in-out', 'type': 'text'}),   
    )
    content_reply = forms.CharField(
        widget= forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm rounded-lg border bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500', 'type': 'text'}),   
    )