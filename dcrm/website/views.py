from django.shortcuts import render, redirect 
from .forms import CreateUserForm,LoginForm, Ride_booking_form 
from .models import Ride_Bookings
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate 
from django.contrib.auth.decorators import login_required 
from django. contrib import messages 
import requests 
from datetime import datetime  


# Create your views here. 



def home(request): 
    api_key = '5b7b4c756201a012ea2c507e74f5b017' 
    city = 'Krakow' 

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    current_date= datetime.now() 
    formatted_date = current_date.strftime("%b %d/%m/%Y") 

    data = response.json()
    temp= data['main']['temp'] 
    description = data['weather'][0]['description']
    icon_code = data['weather'][0]['icon']

    context = {
                    'date': formatted_date,
                    'temperature': temp,
                    'description': description,
                    'icon_code': icon_code,
        }
    return render(request, 'website/index.html', context= context)




    return render(request, 'website/index.html') 

def register(request): 
    form = CreateUserForm()

    if request.method == "POST": 
        form= CreateUserForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return redirect('login') 

    context = {'form':form}  

    return render(request, 'website/register.html', context=context) 


def mylogin(request): 
    form= LoginForm()  
    if request.method == "POST": 
        form=LoginForm(request, data=request.POST)
        if form.is_valid(): 
            username= request.POST.get('username') 
            password =request.POST.get('password')   

            user = authenticate(request, username=username, password=password) 

            if user is not None: 
                auth.login(request,user) 
                return redirect('') 
    context = {'login_form':form}  
    return render(request, 'website/Login.html', context=context)  

def logout(request): 
    auth.logout(request) 
    return redirect("")  

def about_us(request): 
    return render(request,"website/about_us.html")


@login_required(login_url='my-login') 
def ride(request):  
    form= Ride_booking_form()  
    if request.method == "POST": 
        updated_request= request.POST.copy() 
        updated_request.update({'ride_user_id_id ': request.user}) 

        form= Ride_booking_form(updated_request) 
        print("I am here")
        if form.is_valid(): 
            obj = form.save(commit=False)   
            
            # calculate the amount of date
            arrive= obj.ride_booking_date_arrive 
            depart= obj.ride_booking_date_leave 
            result = depart - arrive 
            print("Number of days: ", result.days) 

            ride_total_cost = int(obj.ride_booking_adults ) *65\
                              +int(obj.ride_booking_children) * 35\
                              +int(obj.ride_booking_oap) * 40  
            
            ride_total_cost *= int(result.days)  

            Ride_points=int(ride_total_cost /20) 
            print("Ride points : ", Ride_points) 
            print("printing booking costs: ", ride_total_cost) 


            # see the values in the data 
            obj.ride_points= Ride_points 
            obj.ride_total_cost = ride_total_cost 
            obj.ride_user_id= request.user 


            obj.save() 

            messages.success(request, "Ride booked successfully") 
            return redirect('') 

        else: 
            print("There was a problem with the form") 
            return redirect("booking1") 
    else:
        print("There is an issue with the post")

    context= {'form':form}  

    return render(request, 'website/bookings.html', context=context) 

@login_required(login_url= 'login') 
def dashboard(request):   
    tablestuff= Ride_Bookings.objects.filter(ride_user_id_id=request.user) 
    context= {'records': tablestuff} 



    return render (request, 'website/dashboard.html', context=context)   


   




            




            



    
