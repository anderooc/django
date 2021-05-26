from django.contrib import admin
from django.urls import path

from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='index'),
    path('viewProfile/', views.viewProfile, name='viewProfile'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('viewAssignments/', views.viewAssignments, name='viewAssignments'),
    path('makeAssignment/', views.makeAssignment, name='makeAssignment'),
    path('signUp/', SignUpView.as_view(), name='signup')
]
