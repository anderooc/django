from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewProfile/', views.viewProfile, name='viewProfile'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('viewAssignment/', views.viewAssignment, name='viewAssignment'),
    path('makeAssignment/', views.makeAssignment, name='makeAssignment')
]
