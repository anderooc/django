from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This BlackBaud")

def editProfile(request)
    return HttpResponse("Edit your profile here")

def viewAssignment(request, assignmentName):
    return HttpResponse(assignmentName)

def makeAssignment(request)
    return HttpResponse("Make your assignment here")
