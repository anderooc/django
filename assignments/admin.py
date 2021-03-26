from django.contrib import admin
from .models import UserProfile, StudentProfile, TeacherProfile, Assignment
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Assignment)
