from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.home, name ='home'),
    path('about',views.about, name='about'),
     path('awareness',views.awareness, name ='awareness'),
      path('contacts',views.contacts, name ='contact'),
     path('hospital',views.hospital, name='hospital'),
     path('statestic', views.statestic, name='statestic'),
     
    
]