from django.shortcuts import render, redirect 
from .forms import CreateUserForm,LoginForm, Ride_booking_form
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate 
from django.contrib.auth.decorators import login_required 
from django. contrib import messages

# Create your views here. 



def home(request): 
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


@login_required(login_url='my-login') 
def ride(request):  
    form= Ride_booking_form()  
   
    if request.method == "POST": 
        updated_request= request.POST.copy() 
        updated_request.method({'ride_user_id_id ': request.user}) 

        form= Ride_booking_form(updated_request) 
        if form.is_valid(): 
            obj = form.save(commit=False)  
            # calculate the amount of date
            arrive= obj.ride_booking_date_arrive 
            depart= obj.ride_booking_date_leave 
            result = arrive-depart 
            print("Number of days: ", result.days) 

            ride_total_cost = int(obj.ride_booking_adults ) *65\
                              +int(obj.ride_booking_children) * 35\
                              +int(obj.hotel_booking_oap) * 40  
            
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

    context= {'form':form}  

    return render(request, 'website/bookings.html', context=context) 





        



    
