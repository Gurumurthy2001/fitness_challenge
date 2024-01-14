from django.http import HttpResponse
from django.shortcuts import render


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
  return render(request,'templates/Fitness/register.html')
  
def login(request):
  return render(request,'templates/Fitness/login.html')
  
def dash(request):
  return render(request,'templates/Fitness/dash.html')
  
  