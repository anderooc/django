from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import UserProfile, StudentProfile, TeacherProfile, Assignment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# This is the homepage view, link is basic link with /assignments/ added
def index(request):
    if request.POST:
        if 'inputUsername' in request.POST.keys():
            user = authenticate(username=request.POST['inputUsername'],
                password=request.POST['inputPassword'])
            if user is not None:
                login(request, user)
            else:
                pass
        elif 'logout' in request.POST.keys():
            logout(request)
    context = {
        'user' : request.user
    }
    return render(request, 'assignments/home.html', context)

# This is the view to look at the profile,
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
                'student': student,
            }
        else:
            teacher = get_object_or_404(TeacherProfile, user=thisUser) # better
            context = {
                'username': username,
                'teacher': teacher,
            }
        return render(request, 'assignments/userProfile.html', context)
    else:
        context = {
        }
        return render(request, 'assignments/signup.html', context)

# This view allows users to edit their own profile
def editProfile(request):
    return render(request, 'assignments/userProfile.html')

# This view allows users to see all active assignments
def viewAssignments(request):
    allAssignments = Assignment.objects.all()
    context = {
        "allAssignments": allAssignments,
    }
    print(context)
    return render(request, 'assignments/assignmentsPage.html', context)

# This view allows teachers to make new assignments
def makeAssignment(request):
    return HttpResponse(request, "Make your assignment here")

#
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'assignments/signup.html'
