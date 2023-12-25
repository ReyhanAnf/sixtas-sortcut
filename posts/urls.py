from . import views
from django.urls import path

urlpatterns = [
    path('', views.posting, name='posting'),
    path('create/', views.create_post, name='create-post'),
    path('<postId>/answer', views.create_answer, name='create-answer'),\
    path('<answerId>/reply', views.create_reply, name='create-reply'),\
]