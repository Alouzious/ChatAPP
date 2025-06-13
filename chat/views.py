from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout   
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import IntegrityError
from django.db.models import Q

# Create your views here.
def welcome(request):
    return render(request, 'chat/welcome.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'chat/registered.html')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'chat/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'chat/register.html', {'error': 'Passwords do not match'})

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            return redirect('chat:profile')  # or wherever you want to redirect after login

        except IntegrityError:
            return render(request, 'chat/register.html', {'error': 'Username already exists'})

    return render(request, 'chat/register.html')

@login_required
def profile(request):
    return render(request, 'chat/welcome.html')
@login_required
def logout(request):
    auth_logout(request)
    return render(request, 'chat/welcome.html')

@login_required
def registered_users(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/registered_users.html', {'users': users})



