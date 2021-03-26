from django.shortcuts import render
from django.template import loader
from .models import Assignment
from django.contrib.auth.models import User, Profile, StudentProfile, TeacherProfile
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {
        'user' : request.user
    }
    return render(request, 'assignments/home.html', context)

def viewProfile(request):
    user = User.objects.get(username = usr)
    isStudent = get_object_or_404(Profile, pk=is_student)
    if isStudent:
        grade = get_object_or_404(StudentProfile, pk=grade)
    else:
        subject = get_object_or_404(TeacherProfile, pk=subject)
    context = {
        'username': usr,
        'grade': grade,
        'subject': subject
    }
    return render(request, 'assignments/userProfile.html', context)

def editProfile(request):
    return render(request, 'assignments/userProfile.html')

def viewAssignment(request, assignmentName):
    name  = get_object_or_404(Assignment, pk=assignmentName)
    description = get_object_or_404(Assignment, pk=assignmentDescription)
    context = {
        'name': name,
        'description': description
    }
    return HttpResponse(request, assignmentName, context)

def makeAssignment(request):
    return HttpResponse(request, "Make your assignment here")
