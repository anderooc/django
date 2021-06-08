from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewProfile/', views.viewProfile, name='viewProfile'),
    path('viewAssignments/', views.viewAssignments, name='viewAssignments'),
    path('makeAssignments1/', views.makeAssignments1, name='makeAssignment1'),
    path('makeAssignments/', views.makeAssignments, name='makeAssignment'),
    path('signUp/', views.signup, name='signup'),
    path('changePassword1/', views.changePassword1, name='changePassword1'),
    path('changePassword/', views.changePassword, name='changePassword')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
