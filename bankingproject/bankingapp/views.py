from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# from .forms import Valueform

def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1= request.POST.get('password')
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request, user)
            return render(request,'welcome.html')
        else:
            messages.info(request,"invalid data")
            return render(request,'login.html')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password1')
        if password1==password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,"Username Taken")
               return render(request,'register.html')
           else:
               user = User.objects.create_user(username=username,password=password1)
               user.save()
               return render(request,'login.html')
        else:
           messages.info(request, "password not matching")
           return render(request,'register.html')
    return render(request, "register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')

def welcome(request):
    return render(request,'welcome.html')
def form(request):
    return render(request,'form.html')
# def Valueform(request):
#     context ={}
#     context['form']= Valueform()
#     return render(request, "form.html", context)
