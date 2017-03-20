from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=120, unique=True)
    pwd= models.CharField(max_length=80)
    #no_of_topics=models.IntegerField(default=0)
    #type_user=models.IntegerField(default=0) #simple=0 org=1
    def __str__(self):
        return self.user_name

