from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import UserProfile, StudentProfile, TeacherProfile, Assignment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .forms import SignupForm, ChangePasswordForm, MakeAssignmentsForm
from django.contrib.auth.password_validation import validate_password, password_changed, ValidationError

# This is the homepage view, link is basic link with /assignments/ added
def index(request):
    # Checks if there is data in form
    if request.POST:
        # Checks to make sure form is the login form
        if 'inputUsername' in request.POST.keys():
            # Try to authenticate user with submitted username and password
            user = authenticate(username=request.POST['inputUsername'], password=request.POST['inputPassword'])
            # Login if authenticated
            if user is not None:
                login(request, user)
            else:
                pass
        # Checks if form is logout form
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
        # Obtains all parts of user object
        username = request.user.username
        thisUser = User.objects.get(username = username)
        thisUserProfile = get_object_or_404(UserProfile, user=thisUser)
        # Checks if user is a student
        if thisUserProfile.is_student:
            # Obtains all parts of student object
            student = get_object_or_404(StudentProfile, student=thisUser)
            context = {
                'username': username,
                'isStudent': thisUserProfile.is_student,
                'student': student,
            }
        # Account is a teacher account if not student
        else:
            # Obtains all parts of teacher object
            teacher = get_object_or_404(TeacherProfile, teacher=thisUser)
            context = {
                'username': username,
                'isStudent': thisUserProfile.is_student,
                'teacher': teacher,
            }
        return render(request, 'assignments/userProfile.html', context)
    else:
        # Takes user to sign up if not authenticated
        context = {
        }
        return render(request, 'assignments/signup.html', context)

# This view allows users to see all active assignments
def viewAssignments(request):
    # Collects all assignments
    allAssignments = Assignment.objects.all()
    context = {
        "allAssignments": allAssignments,
    }
    return render(request, 'assignments/assignmentsPage.html', context)

# This precedes makeAssignments and dodges multivaluedictkeyerror
def makeAssignments1(request):
    # Checks if user is authenticated
    if request.user.is_authenticated:
        username = request.user.username
        thisUser = User.objects.get(username = username)
        thisUserProfile = get_object_or_404(UserProfile, user=thisUser)
        # Returns form and whether user is a student or not
        context = {
            'user' : request.user,
            'MakeAssignmentsForm' : MakeAssignmentsForm,
            "isStudent": thisUserProfile.is_student
        }
        return render(request, 'assignments/makeAssignments.html', context)
    else:
        context = {
        }
        return render(request, 'assignments/index.html', context)


# This view allows teachers to make new assignments
def makeAssignments(request):
    # Obtains all parts of user object
    username = request.user.username
    thisUser = User.objects.get(username = username)
    thisUserProfile = get_object_or_404(UserProfile, user=thisUser)
    # Returns form and whether user is a student or not
    context = {
            "MakeAssignmentsForm": MakeAssignmentsForm,
            "isStudent": thisUserProfile.is_student
    }
    # Creates new assignment object with name and description from form
    assignment = Assignment(
        assignmentName = request.POST['name'],
        assignmentDescription = request.POST['description']
    )
    assignment.save()

    return render(request, 'assignments/makeAssignments.html', context)

# This view allows new users to sign up over a form
def signup(request):
    # Calls form made in forms.py
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # Validates no conditions failed
        if form.is_valid():
            # Saves new user with username and password
            newUser = User(
                username = request.POST['username'],
                password = make_password(request.POST['password1']),
            )
            newUser.save()
            # In case of synchronism issue
            newUser.refresh_from_db()

            # is_student and is_teacher are either "on" or "off"; changes to booleans
            if request.POST.get("is_student", False) == "on":
                formIsStudent = True
            else:
                formIsStudent = False
            if request.POST.get("is_teacher", False) == "on":
                formIsTeacher = True
            else:
                formIsTeacher = False

            # Creates new profile given user and account type (in booleans)
            profile = UserProfile(
                user = newUser,
                is_student = formIsStudent,
                is_teacher = formIsTeacher
            )
            profile.save()

            # Creates new student profile if account type is student
            if formIsStudent:
                student = StudentProfile(
                    student = newUser,
                    grade = 0 # Default
                )
                student.save()
            # Creates new teacher account if account type is teacher
            else:
                teacher = TeacherProfile(
                    teacher = newUser,
                    subject = "unknown" # Default
                )
                teacher.save()

            # Redirects to homepage to sign in
            return redirect("index")

    return render(request, 'assignments/signup.html', {'form': form})

# This precedes changePassword and dodges multivaluedictkeyerror
def changePassword1(request):
    context = {
        'user' : request.user,
        'ChangePasswordForm' : ChangePasswordForm,
    }
    return render(request, 'assignments/changePassword.html', context)

# This view allows users to change their password
def changePassword(request):
    newPassword = request.POST['password']
    # Checks if password fits all validation conditions in djproject/settings.py
    try:
        validate_password(newPassword, user=request.user)
    # If passwords does not pass all conditions refresh form
    except ValidationError:
        context = {
            'user' : request.user,
            'ChangePasswordForm' : ChangePasswordForm,
        }
        return render(request, 'assignments/changePassword.html', context)

    # set_password hashes password automatically
    request.user.set_password(newPassword)
    # Saves new passworsd
    request.user.save()
    # Tells all validators that previous password is freed up
    password_changed(newPassword, user=request.user)

    # Obtains all parts of user object
    username = request.user.username
    thisUser = User.objects.get(username = username)
    thisUserProfile = get_object_or_404(UserProfile, user=thisUser)

    # Returns based off of account type
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
