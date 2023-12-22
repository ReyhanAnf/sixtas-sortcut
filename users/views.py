from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
from logreg import forms as lrforms
from django.contrib.auth.models import User
from .models import Person

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
    
def add_profile(request):
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
      
      success= "user " + username + " telah sukses di edit"
      #models.Person.objects.create(nis=nis, email=email, jenis_kelamin=jenis_kelamin, kelas=kelas, jurusan=jurusan, hobi=hobi)
      return redirect('../edit')
    
  return render(request, 'person/edit_profil.html', {'form': form,'formAuth':formAuth, 'username': username, 'succes':""})


def get_data_user_person():
  userperson = [
      ]
  person_data = Person.objects.values_list("nis", "kelas", "jurusan", "jenis_kelamin", "hobi")
    
  for i in range(len(person_data)):
      basicinfo = User.objects.get(username=person_data[i][0])
      otherinfo = person_data[i]
      data_profile  = {
        "nis": basicinfo.username,
        "nama_lengkap": basicinfo.first_name,
        "nama_panggilan": basicinfo.last_name,
        "kelas" : otherinfo[1],
        "jurusan" : otherinfo[2],
        "jenis_kelamin" : otherinfo[3],
        "hobi" : otherinfo[4],
      }
      
      userperson.append(data_profile)
  return userperson

