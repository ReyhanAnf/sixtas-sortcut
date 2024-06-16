from django.shortcuts import render, redirect
from django.contrib.auth import logout
from logreg import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import Person
from posts.views import posts_data
from predictfakenews import forms as pf
from predictfakenews.views import predictPage


# Create your views here.
def index(request):
    form = forms.FormLogin()
    if request.method == 'POST' and request.POST.get("loginbtn") == "loginbtn":
      print(request.POST.get("loginbtn"))
      username = request.POST['username']
      
      if User.objects.filter(username=username).exists():
          return redirect('../user/login/' + username + '/')
      else:
          return redirect('../user/register/' + username + '/')
    
    
    postsData = posts_data()
    formpred = pf.FormPredict()
    predict = predictPage(request)
    
    if predict != None:
      return render(request, 'index.html', {'form': form, 'content': {'title':'Reyhan Anf'}, "form_pred" : formpred, "scrap": predict[0], "title": predict[1], "prediksi": predict[2], "cposts" : postsData})
    else:
      return render(request, 'index.html', {'form': form, 'content': {'title':'Reyhan Anf'}, "form_pred" : formpred, "scrap": None, "title": None, "prediksi": None, "cposts" : postsData})
    

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
  postsData = posts_data()
  
  if request.user.username:
    form = pf.FormPredict()
    predict = predictPage(request)
    
    if predict != None:
      return render(request, 'dashboard.html',{'content': request.user, "cposts" : postsData, "form": form, "scrap": predict[0], "title": predict[1], "prediksi": predict[2]})
    else:
      return render(request, 'dashboard.html',{'content': request.user, "cposts" : postsData, "form": form, "scrap": None, "title": None, "prediksi": None})
  else:
    return redirect('welcome')
    



