from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 
from .models import Ride_Bookings

from django import forms 
from django.forms.widgets import PasswordInput, TextInput 

#- register or create a user 

class CreateUserForm(UserCreationForm): 
    class Meta: 
        model= User 
        fields= ['username', 'password1', 'password2'] 



#login user 
class LoginForm(AuthenticationForm): 
    username= forms.CharField(widget= TextInput()) 
    password= forms.CharField(widget= PasswordInput())  

# Ride booking 

class Ride_booking_form(forms.ModelForm): 
     class Meta: 
         model=  Ride_Bookings   

         fields=['ride_booking_date_arrive', 'ride_booking_date_leave', 'ride_booking_adults', 
                 'ride_booking_children', 'ride_booking_oap', 'ride_total_cost', 'ride_points']  
         label = { 
             "ride_booking_date_arrive": "Day you wish to arrive", 
         } 
         widgets = { 
              'ride_booking_date_arrive': forms.DateInput(attrs={'type':'date'}), 
              'ride_booking_date_leave' : forms.DateInput(attrs= {'type':'date'}),   
              'ride_total_cost': forms.HiddenInput(), 
              'ride_points' :forms.HiddenInput(), 




         } 
def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)


    
    