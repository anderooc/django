from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class studentProfile(models.Model):
    name = models.CharField(max_length=75)
    grade = models.IntegerField()
                            
    
class teacherProfile(models.Model):
    name = models.CharField(max_length=75)
    subject = models.CharField(max_length=50)

class Assignment(models.Model):
    assignmentName = models.CharField(max_length=100)
    
