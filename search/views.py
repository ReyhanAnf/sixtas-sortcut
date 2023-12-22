from django.shortcuts import render
from users.views import get_data_user_person

# Create your views here.
def search_user(request):
  users_data = []
  message = "Search by NIS or Name"
  if request.method == "POST":
    search_user = request.POST["search_user"]
    getting_users = get_data_user_person(search_user)
    for i in getting_users:
      fetch = {
        'nis': i['nis'],
        'nama_lengkap': i['nama_lengkap'],
      }
      users_data.append(fetch)
      message = "You have search for keyword : " + search_user
  else:
    message = "Search by NIS or Name"
    
  return render(request, "search/search.html", {'content':users_data, "message":message})

def preview_search_user(request, nis_search):
  user_search = get_data_user_person(nis_search)[0]
  return render(request, "search/preview.html", {'content':user_search})