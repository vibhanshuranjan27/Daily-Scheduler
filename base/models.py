from operator import truediv
from django.db import models
from django.contrib.auth.models import User #takes care of user info; This is how Django takes care of authentication 
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True) #tasks get deleted if account is deleted by admin or user
    title = models.CharField(max_length= 200)
    description = models.TextField(null= True, blank=True)
    complete = models.BooleanField(default= False)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete'] #sets the completed tasks to the bottom