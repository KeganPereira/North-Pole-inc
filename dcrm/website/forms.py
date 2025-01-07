from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User  
from django.core.validators import MinValueValidator
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
        model = Ride_Bookings
        fields = [
            'ride_booking_date_arrive', 'ride_booking_date_leave',
            'ride_booking_adults', 'ride_booking_children',
            'ride_booking_oap', 'ride_total_cost', 'ride_points'
        ]
        labels = {
            "ride_booking_date_arrive": "Day you wish to arrive",
        }
        widgets = {
            'ride_booking_date_arrive': forms.DateInput(attrs={'type': 'date'}),
            'ride_booking_date_leave': forms.DateInput(attrs={'type': 'date'}),
            'ride_total_cost': forms.HiddenInput(),
            'ride_points': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

    def clean_ride_booking_children(self): 
        #Access the fields value 
        children = self.cleaned_data.get('ride_booking_children') 
        if children is not None and children<0: 
            raise forms.ValidationError('The number of children cannot negative') 
        return children 
    
    def clean_ride_booking_adults(self): 
        #Access the fields value 
        adults = self.cleaned_data.get('ride_booking_adults') 
        if adults is not None and adults<0: 
            raise forms.ValidationError('The number of  adults cannot negative') 
        return adults 
    
    def clean_ride_booking_oaps(self): 
        oaps = self.cleaned_data.get('ride_booking_oaps') 
        if oaps is not None and oaps<0: 
           raise forms.ValidationError('the number of oap cannot be negative') 
        return oaps