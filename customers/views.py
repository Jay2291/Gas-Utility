# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import ServiceRequestForm
from .forms import UserSignupForm
# from django.contrib.auth.models import User
from django.contrib.auth import login

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ServiceRequestForm
from .models import ServiceRequest
# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def my_view(request):
    # If the form was submitted (POST request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user using the provided credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # If user is found and active, log the user in
            if user.is_active:
                login(request, user)
                # Redirect the user to the homepage after successful login
                return redirect('home')  # Assuming 'home' is the name of your home view
            else:
                # If the user is not active
                return render(request, 'login.html', {'error': 'Account is not active.'})
        else:
            # If authentication failed (invalid username or password)
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        # If it's a GET request, render the login form
        return render(request, 'login.html')

@login_required
def customer_home(request): 
    return render(request, 'customers/customer_home.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')  
    else:
        profile_form = UserProfileForm(instance=request.user)
    return render(request, 'customers/edit_profile.html', {'profile_form': profile_form})

@login_required
def add_service_request(request):
    if request.method == 'POST':
        service_request_form = ServiceRequestForm(request.POST, request.FILES)
        if service_request_form.is_valid():
            service_request = service_request_form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('home') 
    else:
        service_request_form = ServiceRequestForm()
    return render(request, 'customers/add_service_request.html', {'service_request_form': service_request_form})

@login_required
def track_requests(request):
    # Retrieve all service requests for the logged-in user
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customers/track_requests.html', {'service_requests': service_requests})

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect after successful signup
    else:
        form = UserSignupForm()
    return render(request, 'registration/signup.html', {'form': form})