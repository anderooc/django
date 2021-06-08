from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import UserProfile, StudentProfile, TeacherProfile, Assignment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .forms import SignupForm, ChangePasswordForm
from django.contrib.auth.password_validation import validate_password, password_changed, ValidationError

# This is the homepage view, link is basic link with /assignments/ added
def index(request):
    if request.POST:
        if 'inputUsername' in request.POST.keys():
            user = authenticate(username=request.POST['inputUsername'], password=request.POST['inputPassword'])
            if user is not None:
                login(request, user)
            else:
                pass
        elif 'logout' in request.POST.keys():
            logout(request)
    context = {
        'user' : request.user,
        'ChangePasswordForm' : ChangePasswordForm
    }
    return render(request, 'assignments/home.html', context)

# This is the view to look at the profile,
def viewProfile(request):
    if request.user.is_authenticated:
        username = request.user.username
        thisUser = User.objects.get(username = username)
        thisUserProfile = get_object_or_404(UserProfile, user=thisUser)
        if thisUserProfile.is_student:
            student = get_object_or_404(StudentProfile, student=thisUser)
            context = {
                'username': username,
                'isStudent': thisUserProfile.is_student,
                'student': student,
            }
        else:
            teacher = get_object_or_404(TeacherProfile, teacher=thisUser)
            context = {
                'username': username,
                'isStudent': thisUserProfile.is_student,
                'teacher': teacher,
            }
        return render(request, 'assignments/userProfile.html', context)
    else:
        context = {
        }
        return render(request, 'assignments/signup.html', context)

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
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            newUser = User(
                username = request.POST['username'],
                password = make_password(request.POST['password1']),
            )
            newUser.save()
            newUser.refresh_from_db()

            if request.POST.get("is_student", False) == "on":
                formIsStudent = True
            else:
                formIsStudent = False

            if request.POST.get("is_teacher", False) == "on":
                formIsTeacher = True
            else:
                formIsTeacher = False
            profile = UserProfile(
                user = newUser,
                is_student = formIsStudent,
                is_teacher = formIsTeacher
            )
            profile.save()
            if formIsStudent:
                student = StudentProfile(
                    student = newUser,
                    grade = 0
                )
                student.save()
            else:
                teacher = TeacherProfile(
                    teacher = newUser,
                    subject = "unknown"
                )
                teacher.save()
            return redirect("index")
    return render(request, 'assignments/signup.html', {'form': form})

def changePassword1(request):
    context = {
        'user' : request.user,
        'ChangePasswordForm' : ChangePasswordForm,
    }
    return render(request, 'assignments/changePassword.html', context)

def changePassword(request):
    newPassword = request.POST['password']
    try:
        validate_password(newPassword, user=request.user)
    except ValidationError:
        context = {
            'user' : request.user,
            'ChangePasswordForm' : ChangePasswordForm,
        }
        return render(request, 'assignments/changePassword.html', context)
    request.user.set_password(newPassword)
    request.user.save()
    password_changed(newPassword, user=request.user)
    username = request.user.username
    thisUser = User.objects.get(username = username)
    thisUserProfile = get_object_or_404(UserProfile, user=thisUser)
    if thisUserProfile.is_student:
        student = get_object_or_404(StudentProfile, student=thisUser)
        context = {
            'username': username,
            'isStudent': thisUserProfile.is_student,
            'student': student,
            'ChangePasswordForm': ChangePasswordForm,
        }
    else:
        teacher = get_object_or_404(TeacherProfile, teacher=thisUser)
        context = {
            'username': username,
            'isStudent': thisUserProfile.is_student,
            'teacher': teacher,
            'ChangePasswordForm': ChangePasswordForm,
        }
    return render(request, 'assignments/userProfile.html', context)
