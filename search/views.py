from django.shortcuts import render
from users.views import get_data_user_person

# Create your views here.
def index(request):
  users_data = []
  message = ""
  if request.method == "POST":
    search_user = request.POST["search_user"]
    getting_users = get_data_user_person(search_user)
    for i in getting_users:
      fetch = {
        'nis': i['nis'],
        'nama_lengkap': i['nama_lengkap'],
      }
      users_data.append(fetch)
  else:
    message = "Ayo Cari Temanmu"
    
  print(users_data)
  return render(request, "search/search.html", {'content':users_data, "message":message})