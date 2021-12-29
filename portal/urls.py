from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

#urlpatterns

urlpatterns = [
    path('', views.login_view),
    path('login/', views.login_view),
    path('signup/', views.register_view),
    path('register/', views.register),          
    path('index/', views.login),
    path('index/<str:user>/profile/', views.view_profile),
    path('index/<str:user>/subjects/', views.view_subjects),
    path('index/<str:user>/dashboard/', views.view_profile),        
    path('index/<str:user>/new/', views.view_lecture),
    path('index/<str:user>/lectures/', views.view_lecture),
    path('index/<str:user>/lecture/', views.view_lecture),
    path('index/<str:user>/attendence/', views.view_attendance),
    path('index/<str:user/lectures/', views.view_lecture),
    path('index/<str:user>/profile-edit/', views.edit_profile),
    path('index/<str:user>/mark-attendence/', views.mark_attendance),    
]
