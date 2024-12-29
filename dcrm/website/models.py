from django.db import models 

from django.contrib.auth.models import AbstractUser  
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser): 
    points = models.IntegerField(default=0) 
    address=models.CharField(max_length=200, blank=True) 
    phone = models.CharField(max_length=14, blank=True) 

class Ride_Bookings(models.Model): 
    booking_id = models.AutoField(primary_key=True, editable= False) 
    ride_user_id= models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    ride_booking_date= models.DateField(auto_now_add= True) 
    ride_booking_date_arrive=models.DateField()  
    ride_booking_date_leave= models.DateField() 
    ride_booking_adults=models.IntegerField(default=0, validators=[MinValueValidator(0)])
    ride_booking_children=models.IntegerField(default=0, validators= [MinValueValidator(0)]) 
    ride_booking_oap= models.IntegerField(default=0, validators= [MinValueValidator(0)]) 
    ride_total_cost= models.FloatField(default=0) 
    ride_points= models.IntegerField(default=0) 




# Create your models here.
