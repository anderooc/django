from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import UserProfile, StudentProfile, TeacherProfile, Assignment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {
        'user' : request.user
    }
    return render(request, 'assignments/home.html', context)

def viewProfile(request):
    user = User.objects.get(username = usr)
    isStudent = get_object_or_404(UserProfile, pk=is_student)
    if isStudent:
        student = get_object_or_404(StudentProfile, pk=user)
        context = {
            'username': usr,
            'isStudent': isStudent,
            'student': student
        }
    else:
        teacher = get_object_or_404(TeacherProfile, pk=user)
        context = {
            'username': usr,
            'teacher': teacher
        }
    return render(request, 'assignments/userProfile.html', context)

def editProfile(request):
    return render(request, 'assignments/userProfile.html')

def viewAssignment(request):
    name  = get_object_or_404(Assignment, pk=assignmentName)
    description = get_object_or_404(Assignment, pk=assignmentDescription)
    context = {
        'name': name,
        'description': description
    }
    return HttpResponse(request, 'assignments/assignmentPage.html', context)

def makeAssignment(request):
    return HttpResponse(request, "Make your assignment here")
