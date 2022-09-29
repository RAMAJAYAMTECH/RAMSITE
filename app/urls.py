from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name="home"),
    #path('services',views.services,name="services"),
    #path('employee',views.employee,name="employee"),
    #path('feedback',views.feedback,name="feedback"),
    #path('about',views.about,name="about"),

]