from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.contrib.auth.models import User
from users.models import Person

# Create your views here.
def login_view(request, username):
    form = forms.FormLogin()
    user_used = username
    if request.method == 'POST':
        username = user_used
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('../../../')
    return render(request, 'login/login.html', {'form': form, 'user_used':user_used})

def register_view(request, username):
    form = forms.FormRegister()
    user_new = username
    
    if request.method == 'POST':
        username = user_new
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        
        if username and password == confirm_password and first_name and last_name:
            User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            Person.objects.create(nis=username, jenis_kelamin="", kelas="", jurusan="", bio="")
        else:
          status = True
          return render(request, 'login/register.html', {'form': form, 'user_new':user_new, 'status': status})
            
        if authenticate(request, username=username, password=password):
            user = authenticate(request, username=username, password=password)
            login(request, user)
            
            return redirect('../../../')
    return render(request, 'login/register.html', {'form': form, 'status': False})


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('main')