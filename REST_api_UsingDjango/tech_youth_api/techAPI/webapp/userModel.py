from django.db import models
# import datetime
from . interestModel import *
# Create your models here.
class user(models.Model):
    user_id=models.AutoField(primary_key=True,max_length=40)
    username=models.CharField(max_length=40)
    emailid=models.CharField(unique=True,max_length=40)
    password=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.emailid}"