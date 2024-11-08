from django.urls import path
from app import views


urlpatterns = [ 
               
    path('', views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('home/',views.home, name="home"),
    ]
