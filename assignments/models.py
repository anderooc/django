from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(User):
    user = models.OneToOneField(

    )
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    grade = models.IntegerField()

class TeacherProfile(models.Model):
    subject = models.CharField(max_length=50)

class Assignment(models.Model):
    assignmentName = models.CharField(max_length=100)
