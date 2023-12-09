from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
from logreg import forms as lrforms
from django.contrib.auth.models import User

# Create your views here.
def users(request):
    return HttpResponse("All Users done Viewed")
    
def profil_btn(request):
  if request.user:
    user = request.user
    print(user)
    return redirect('../../' + user.username + '/')
  else:
    return redirect("welcome")
 
   
def profil_view(request, username):
  if username == request.user.username:
    print(models.Person.objects.get(nis=request.user.username))
    return render(request, 'person/profil.html', {'user': request.user, 'person':models.Person.objects.get(nis=request.user.username)})
  else:
    return redirect('../' + request.user.username + '/')
    
def add_profil(request):
  username = request.user.username
  person = models.Person()
  nis = username
  user_change = models.Person.objects.get(nis=username)
  userAuth_change = User.objects.get(username=nis)
  
  form = forms.FormProfil(initial={'jenis_kelamin':user_change.jenis_kelamin,'kelas':user_change.kelas, 'jurusan':user_change.jurusan,'hobi':user_change.hobi})
  formAuth = lrforms.FormRegister(initial={'email':userAuth_change.email})
  
  if request.method == 'POST':
    nis = nis
    email = request.POST['email']
    jenis_kelamin = request.POST['jenis_kelamin']
    kelas = request.POST['kelas']
    jurusan = request.POST['jurusan']
    hobi = request.POST['hobi']
    
    
    if nis == username:
      user_change.nis = username
      userAuth_change.email = email
      user_change.jenis_kelamin = jenis_kelamin
      user_change.kelas = kelas
      user_change.jurusan = jurusan
      user_change.hobi = hobi
      user_change.save()
      userAuth_change.save()
      
      #models.Person.objects.create(nis=nis, email=email, jenis_kelamin=jenis_kelamin, kelas=kelas, jurusan=jurusan, hobi=hobi)
      return redirect('../../../' + username + "/")
      
  return render(request, 'person/edit_profil.html', {'form': form,'formAuth':formAuth, 'username': username})
