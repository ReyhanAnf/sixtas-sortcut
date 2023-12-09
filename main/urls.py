from django.urls import path, re_path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('welcome/', views.index, name='welcome'),
    path('', views.dashboard, name='main'),
]