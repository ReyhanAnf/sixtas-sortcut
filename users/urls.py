from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('profil/', views.profil_btn, name='profil'),
    path('profil/edit/', views.add_profile, name='add_profil'),
]