from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(User):
    name = models.CharField(max_length=75)
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
    def __str__(self):
        return self.name

class studentProfile(models.Model):
    grade = models.IntegerField()

class teacherProfile(models.Model):
    subject = models.CharField(max_length=50)

class Assignment(models.Model):
    assignmentName = models.CharField(max_length=100)
