from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def register(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username already Exists!")
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already Exists!")
            else:
                data = User.objects.create_user(username=username, password=password, email=email)
                messages.success(request,"User Created Successfully!")
                user = authenticate(username=username,password=password)
                auth_login(request,user)
                return redirect('/')


            
    return render(request,'myapp/register.html',{'messages':messages})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        auth_login(request,user)
        return redirect('/')
    return render(request,'myapp/login.html')