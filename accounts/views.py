 
from .models import User
from .forms import CustomUserCreationForm
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.urls import reverse
from .auth import unauthenticated_user, admin_only
def home(request):
    return render(request, 'accounts/home.html')




def handler404(request, *args, **kwargs):
    return render(request, '404.html', status=404)

def logout(request):
    request.session.flush()
    return redirect('login')

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['inputUsername']
        password = request.POST['inputChoosePassword']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            auth.login(request, user)
            if user.is_superuser:
                return redirect(reverse('admin:index'))

            else:
                return redirect('dashboard')
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    role = request.user.role
    if role == 'secondary_student':
        return render(request, 'secondarystudents/dashboard/secondary_student.html')
    elif role == 'tertiary_student':
        return render(request, 'tertiarystudents/dashboard/tertiary_student.html')
    elif role == 'adult':
        return render(request, 'adults/dashboard/adult.html')
    else:
        return redirect('login')
