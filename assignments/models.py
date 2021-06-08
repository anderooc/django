from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    grade = models.IntegerField()

class TeacherProfile(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    subject = models.CharField(max_length=50)

class Assignment(models.Model):
    assignmentName = models.CharField(max_length=100)
    assignmentDescription = models.CharField(max_length=200)
