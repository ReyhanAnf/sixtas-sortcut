from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
from logreg import forms as lrforms
from django.contrib.auth.models import User
from .models import Person
from django.db.models import Q

# Create your views here.
def users(request):
    return HttpResponse("All Users done Viewed")
    
def profil_btn(request):
  if request.user:
    user = request.user
    return redirect('../../' + user.username + '/')
  else:
    return redirect("welcome")
 
   
def profil_view(request, username):
  if username == request.user.username:
    # print(models.Person.objects.get(nis=request.user.username))
    return render(request, 'person/profil.html', {'user': request.user, 'person':models.Person.objects.get(nis=request.user.username)})
  else:
    return redirect('../' + request.user.username + '/')
    
def add_profile(request):
  username = request.user.username
  person = models.Person()
  nis = username
  user_change = models.Person.objects.get(nis=username)
  userAuth_change = User.objects.get(username=nis)
  
  form = forms.FormProfil(initial={'jenis_kelamin':user_change.jenis_kelamin,'kelas':user_change.kelas, 'jurusan':user_change.jurusan,'bio':user_change.bio})
  formAuth = lrforms.FormRegister(initial={'email':userAuth_change.email})
  
  if request.method == 'POST':
    nis = nis
    email = request.POST['email']
    jenis_kelamin = request.POST['jenis_kelamin']
    kelas = request.POST['kelas']
    jurusan = request.POST['jurusan']
    bio = request.POST['bio']
    
    
    if nis == username:
      user_change.nis = username
      userAuth_change.email = email
      user_change.jenis_kelamin = jenis_kelamin
      user_change.kelas = kelas
      user_change.jurusan = jurusan
      user_change.bio = bio
      user_change.save()
      userAuth_change.save()
      
      success= "user " + username + " telah sukses di edit"
      #models.Person.objects.create(nis=nis, email=email, jenis_kelamin=jenis_kelamin, kelas=kelas, jurusan=jurusan, hobi=hobi)
      return redirect('../edit')
    
  return render(request, 'person/edit_profil.html', {'form': form,'formAuth':formAuth, 'username': username, 'succes':""})


def get_data_user_person(filters="all"):
  userperson = [
      ]
  if filters == "all":
    users_data = User.objects.all()
  elif filters != "all":
    if User.objects.filter(Q(username__icontains=filters) | Q(first_name__icontains=filters)).exists():
        users_data = User.objects.filter(
          Q(username__icontains=filters) | Q(first_name__icontains=filters)
          )
    else:
        users_data = User.objects.all()
    
  
  for user in users_data:
    person_info = Person.objects.get(nis=user.username)
    data_profile  = {
      "nis": user.username,
      "nama_lengkap": user.first_name,
      "nama_panggilan": user.last_name,
      "kelas" : person_info.kelas,
      "jurusan" : person_info.jurusan,
      "jenis_kelamin" : person_info.jenis_kelamin,
      "bio" : person_info.bio,
    }
    userperson.append(data_profile)
  
  return userperson

