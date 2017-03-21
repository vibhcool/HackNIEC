from django.db import models
from django.utils import timezone


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=120, unique=True)
    pwd= models.CharField(max_length=80)
    #no_of_topics=models.IntegerField(default=0)
    #type_user=models.IntegerField(default=0) #simple=0 org=1
    def __str__(self):
        return self.user_name

class studentProfile(models.Model):
    """Profile for a user to store roll number and other details."""
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=120, unique=True)
    roll_number = models.CharField(max_length=20)
    institute = models.CharField(max_length=128)
    department = models.CharField(max_length=64)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
