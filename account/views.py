from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def RegisterView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. Login now")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = RegisterForm()

    return render(request, 'account/register.html', {'form': form})

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username exists
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to a home page or dashboard
            else:
                messages.error(request, "Incorrect password.")
        else:
            messages.error(request, "Username does not exist.")
    
    return render(request, 'account/login.html')

def LogoutView(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('index')