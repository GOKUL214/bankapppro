from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Form



# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        compass=request.POST['cpass']

        if password == compass:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('saved')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request,'Invalid person')
            return redirect('login')

    return render(request,'login.html')

def new(request):
    return render(request,'new.html')
def formpage(request):
    if request.method == 'POST':

        return redirect('submit')

    return render(request,'formpage.html')
def submit(request):
    return render(request,'submit.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

