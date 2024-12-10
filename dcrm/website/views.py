from django.shortcuts import render, redirect 
from .forms import CreateUserForm, LoginForm 
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate

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

        



    