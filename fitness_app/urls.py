from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path("", views.index, name="landing"),
  path("home/", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("contact/", views.contact, name="contact"),
  path("register/",views.register,name="register"),
  path('login/', auth_views.LoginView.as_view(template_name='templates/Fitness/login.html'), name='login'),
  path("logout/", views.logout, name="logout"),
  path("profile/", views.profile, name="profile"),
  path("update", views.updateprofile, name="profileupdate"),
 
]