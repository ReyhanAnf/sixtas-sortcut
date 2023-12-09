from django.urls import path
from . import views

urlpatterns = [
    path('login/<username>/', views.login_view, name='login'),
    path('register/<username>/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]