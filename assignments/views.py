from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
    if request.user.is_authenticated:
        username = request.user.username
        thisUser = User.objects.get(username = username)
        isStudent = get_object_or_404(UserProfile, pk=thisUser.pk)
        if isStudent:
            student = get_object_or_404(StudentProfile, pk=thisUser.pk)
            context = {
                'username': username,
                'isStudent': isStudent,
                'student': student
            }
        else:
            teacher = get_object_or_404(TeacherProfile, user=thisUser) # better
            context = {
                'username': username,
                'teacher': teacher
            }
        return render(request, 'assignments/userProfile.html', context)
    else:
        return HttpResponse("User login not found")

def editProfile(request):
    return render(request, 'assignments/userProfile.html')

def viewAssignments(request):
    allAssignments = Assignment.objects.all()
    context = {
        "allAssignments": allAssignments,
    }
    print(context)
    return render(request, 'assignments/assignmentsPage.html', context)

def makeAssignment(request):
    return HttpResponse(request, "Make your assignment here")
