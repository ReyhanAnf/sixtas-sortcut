"""
URL configuration for sixtasSortcut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import main
import users
from users import views as users
#from api.views import *

# router = routers.DefaultRouter()
# router.register(r'userp', UserViewSet, basename="userp")
# router.register(r'person', PersonViewSet, basename="person")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('user/', include('logreg.urls')),
    #path('api/', include(router.urls)),
    path('search/', include('search.urls') , name="search"),
    path('posting/', include('posts.urls')),
    
    path('<username>/', users.profil_view),
    #path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
]


