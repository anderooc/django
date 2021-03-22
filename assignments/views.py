from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'assignments/home.html')

def viewProfile(request):
    return render(request, 'assignments/userProfile.html')

def editProfile(request):
    return render(request, 'assignments/userProfile.html')

def viewAssignment(request, assignmentName):
    return HttpResponse(assignmentName)

def makeAssignment(request):
    return HttpResponse("Make your assignment here")
