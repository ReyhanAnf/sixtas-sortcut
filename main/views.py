from django.shortcuts import render, redirect
from django.contrib.auth import logout
from logreg import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import Person
from posts.views import posts_data


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
  postsData = posts_data()
  
  userperson = [
      ]
  if request.user.username:
    # person_data = Person.objects.values_list("nis", "kelas", "jurusan", "jenis_kelamin", "bio")
    # user_data = User.objects.values_list("username", "first_name", "last_name")
    
    
    # for i in range(len(person_data)):
    #    basicinfo = User.objects.get(username=person_data[i][0])
    #    otherinfo = person_data[i]
    #    data_profile  = {
    #       "nama_lengkap": basicinfo.first_name,
    #       "nama_panggilan": basicinfo.last_name,
    #       "kelas" : otherinfo[1],
    #       "jurusan" : otherinfo[2],
    #       "jenis_kelamin" : otherinfo[3],
    #       "hobi" : otherinfo[4],
    #     }
       
    #    userperson.append(data_profile)
    
    return render(request, 'dashboard.html',{'content': request.user, "data_profile": userperson, "cposts" : postsData})
  else:
    return redirect('welcome')
    



