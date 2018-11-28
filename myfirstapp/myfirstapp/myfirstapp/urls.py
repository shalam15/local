"""myfirstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#this is what i need to import to be able to use include just like in php
# so i can include a file in another file
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #so here is the iclude this will include the firstapp.url file
    # basically means it will go to the firstapp and pull from the urls file
    #i could also put the url here but i think it makes sense that we use the urls file from the app we wants to include
    #plus it is in the tutorial i watched :)
    #i still dont know why the first quote is empty though
    path('', include('firstapp.urls'))
]
