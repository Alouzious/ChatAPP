from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout   
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import IntegrityError
from django.db.models import Q
from chat.models import FriendRequest
from django.contrib import messages
from django.conf import settings

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
            return redirect('chat:registered_users')  # Redirect here
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

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings

@login_required
def registered_users(request):
    print("DB path used by server:", settings.DATABASES['default']['NAME'])
    print("Logged in user ID:", request.user.id)

    users = User.objects.exclude(id=request.user.id)
    print(f"Users excluding current user: {list(users)}")

    return render(request, 'chat/registered.html', {'users': users})
@login_required
def send_request(request, user_id):
    sender = request.user
    receiver = get_object_or_404(User, id=user_id)

    # Don't allow self-request
    if sender == receiver:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': "You cannot send a request to yourself."}, status=400)
        messages.error(request, "You cannot send a friend request to yourself.")
        return redirect('chat:registered_users')

    existing_request = FriendRequest.objects.filter(sender=sender, receiver=receiver).first()
    if existing_request:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'info', 'message': "Friend request already sent."}, status=400)
        messages.info(request, "Friend request already sent.")
        return redirect('chat:registered_users')

    # Create friend request
    FriendRequest.objects.create(sender=sender, receiver=receiver)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': f"Friend request sent to {receiver.username}."})
    
    messages.success(request, f"Friend request sent to {receiver.username}.")
    return redirect('chat:registered_users')