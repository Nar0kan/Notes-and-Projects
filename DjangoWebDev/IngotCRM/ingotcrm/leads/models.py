from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    

class Lead(models.Model):
    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    age = models.IntegerField(default=0)

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)    # Every lead has an agent
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     # Every agent has 1 user

    def __str__(self):
        return self.user.email