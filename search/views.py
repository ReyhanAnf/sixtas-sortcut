from django.shortcuts import render
from users.views import get_data_user_person

# Create your views here.
def index(request):
  getting_users = get_data_user_person()
  users_data = []
  for i in getting_users:
    fetch = {
      'nis': i['nis'],
      'nama_lengkap': i['nama_lengkap'],
    }
    users_data.append(fetch)
    
  return render(request, "search/search.html", {'content':users_data})