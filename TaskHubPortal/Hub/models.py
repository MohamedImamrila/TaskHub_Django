from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

def current_time():
    return timezone.now().time()

class CustomUser(AbstractUser):
    Name = models.CharField(max_length=50)
    Phonenumber = models.CharField(max_length=15)
    Address = models.TextField()

    def __str__(self):
        return self.username  # or any other field you want to display

class AddTask(models.Model):
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    TaskName = models.CharField(max_length=100)
    Date = models.DateField(default=timezone.now)
    Time = models.TimeField(default=current_time) 
    AssignedBy = models.TextField()
    Status = models.CharField(max_length=100)

    def __str__(self):
        return self.TaskName
