from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from fitness_app.Forms.forms import UserProfileForm
from fitness_app.models import UserProfile

def index(request):
  context={
    'company':'fitness pvt ltd'
  }
  return render(request,'templates/Fitness/landing.html',context)
  
def home(request):
  return render(request,'templates/Fitness/home.html')
  
def about(request):
  return render(request,'templates/Fitness/about.html')
  
def contact(request):
  return render(request,'templates/Fitness/contact.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Check if a user with the same username or email already exists
        existing_user = User.objects.filter(username=username) or User.objects.filter(email=email)
        if existing_user.exists():
            messages.error(request, 'User with the same username or email already exists.')
            return render(request, 'templates/Fitness/register.html')

        if password == confirm_password:
            # Create the user using get_or_create to handle unique constraints
            user, created = User.objects.get_or_create(username=username, email=email)
            user.set_password(password)
            user.save()

            # Create a corresponding user profile if it doesn't exist
            user_profile, profile_created = UserProfile.objects.get_or_create(user=user)

            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'templates/Fitness/register.html')

  
def login(request):
  return render(request,'templates/Fitness/login.html')
  

def profile(request):
    try:
        user_profile = request.user.userprofile  # Access the user's associated profile
    except UserProfile.DoesNotExist:
        # Handle the case where the profile does not exist
        user_profile = None

    form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page

    return render(request, 'templates/Fitness/profile.html', {'form': form})

def dash(request):
  return render(request,'templates/Fitness/dash.html')

  