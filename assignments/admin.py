from django.contrib import admin
from .models import Profile, StudentProfile, TeacherProfile, Assignment
# Register your models here.

admin.site.register(Profile)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Assignment)
