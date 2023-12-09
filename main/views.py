from django.shortcuts import render, redirect
from django.contrib.auth import logout
from logreg import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    form = forms.FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        
        if User.objects.filter(username=username).exists():
            return redirect('../user/login/' + username + '/')
        else:
            return redirect('../user/register/' + username + '/')
    return render(request, 'index.html', {'form': form, 'content': {'title':'Reyhan Anf'}})

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
  if request.user.username:
    return render(request, 'dashboard.html',{'content': request.user})
  else:
    return redirect('welcome')
    



