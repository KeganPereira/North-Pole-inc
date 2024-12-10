from django.urls import path  
from . import views

urlpatterns = [ 

    path('', views.home, name=""),  
    path('register', views.register, name= "register"), 
    path('login', views.mylogin, name="login") ,
    path('logout', views.logout, name="logout")

]