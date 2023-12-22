from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_user, name='search-user'),
    path('<nis_search>/', views.preview_search_user, name='preview-search-user'),
]