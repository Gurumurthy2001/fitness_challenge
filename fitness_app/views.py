from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from fitness_app.Forms.forms import UserProfileForm,UserRegistrationForm,LoginForm
from fitness_app.models import UserProfile,UserRegistrationForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout  # Importing the correct logout function
from django.views.decorators.cache import cache_control

def index(request):
  context={
    'company':'fitness pvt ltd'
  }
  return render(request,'templates/Fitness/landing.html',context)
  
def home(request):
  return render(request,'templates/Fitness/home.html')
  
def about(request):
  return render(request,'templates/Fitness/about.html')
  
@login_required
def contact(request):
  return render(request,'templates/Fitness/contact.html')


def register(request):
  if request.method == 'POST':
   # breakpoint()
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm-password')
    # Checking if a user with the same username or email already exists
    existing_user = User.objects.filter(Q(username=username) | Q(email=email))

    if existing_user.exists():
      messages.error(request, 'User with the same username or email already exists.')
      return render(request, 'templates/Fitness/register.html')

    if password == confirm_password:
      # Create the user using get_or_create to handle unique constraints
      user, created = User.objects.get_or_create(username=username, email=email)
      user.set_password(password)
      user.save()
      

      # Creating user profile if it doesn't exist
      user_profile, profile_created = UserProfile.objects.get_or_create(user=user)
      user_profile.bio_line = request.POST.get('bio', '') 
      # Assuming 'bio' is part of your registration form
      user_profile.DOB = request.POST.get('dob', None)
      user_profile.save()
      messages.success(request, 'Registration successful. You can now log in.')
      return redirect('login')  
    else:
      messages.error(request, 'Passwords do not match.')

  return render(request, 'templates/Fitness/register.html')


def login(request):
  if request.method =='GET':
    if request.user.is_authenticated:
      return redirect('profile')
      
    form = LoginForm()
    return render(request, 'templates/Fitness/login.html',{'form':form})
     
  elif request.method == 'POST':
    form = LoginForm(request.POST)
    
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
            
      user = authenticate(request,username=username,password=password)
      print("Authenticated user:", user)
      if user:
        #breakpoint()
        login(request, user)
        
        messages.success(request,f'Hi {username.title()}, welcome back!')
        next_url = request.GET.get('next', 'profile')
        return redirect(next_url)
        return redirect('home')
        
    messages.error(request,f'Invalid username or password')
    return render(request,'templates/Fitness/login.html',{'form': form})

@login_required
def profile(request):
  #breakpoint()
  user_profile = get_object_or_404(UserProfile, user=request.user)

  if request.method == 'POST':
    u_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
    if u_form.is_valid():
      u_form.save()
      messages.success(request, 'Profile update successful.')
      return redirect('profile')
    else:
      messages.error(request, 'There was an error updating your profile. Please check the form.')

  else:
    u_form = UserProfileForm(instance=user_profile)

  context = {
        'u_form': u_form
    }

  return render(request, 'templates/Fitness/profile.html', context)


@login_required
def updateprofile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    #print(request.method)

    if request.method == 'POST':
        #breakpoint()
        u_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        print(u_form.errors)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Profile update successful.')
            return redirect('profile')  
        else:
            messages.error(request, 'There was an error updating your profile. Please check the form.')
    else:
        u_form = UserProfileForm(instance=user_profile)

    context = {'u_form': u_form}
    return render(request, 'templates/Fitness/p_update.html', context)

@cache_control(no_cache=True, must_revalidate=True, max_age=0)
def logout(request):
  auth_logout(request)
  messages.success(request, 'You have been logged out.')
  return redirect('landing')